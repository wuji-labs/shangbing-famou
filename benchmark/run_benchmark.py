#!/usr/bin/env python3
"""
ShangBing FaMou Benchmark Runner.

Runs strategy/negotiation/game-theory scenarios across conditions
(baseline, skill, adversarial) and models, collecting each agent response
into a results JSON for later scoring by analyze_results.py.

This runner PRODUCES RAW RESPONSES ONLY. It does not invent or score metrics.
No before/after numbers are ever fabricated. Scoring is a separate step.

Usage:
    python run_benchmark.py --model claude-sonnet-4 --condition all --runs 5
    python run_benchmark.py --model gpt-4o --condition skill --scenario 2
    python run_benchmark.py --model claude-sonnet-4 --condition all --dry-run

Dependencies (install only the SDK for the provider you use):
    pip install anthropic            # for claude-* models
    pip install openai               # for gpt-* models
    pip install google-generativeai  # for gemini-* models
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MODELS = {
    "claude-sonnet-4": {"provider": "anthropic", "model_id": "claude-sonnet-4-20250514"},
    "gpt-4o": {"provider": "openai", "model_id": "gpt-4o"},
    "gemini-2.5-pro": {"provider": "google", "model_id": "gemini-2.5-pro"},
}

CONDITIONS = ["baseline", "skill", "adversarial"]

DEFAULT_RUNS = 5
DEFAULT_OUTPUT_DIR = "results"

# Token budget for a strategy response — generous enough for full SOP output.
MAX_RESPONSE_TOKENS = 2048
# Exponential backoff for transient API errors.
MAX_RETRIES = 3
RETRY_BASE_DELAY_SECONDS = 2.0

BENCHMARK_DIR = Path(__file__).resolve().parent
SKILL_DIR = BENCHMARK_DIR.parent
SCENARIOS_PATH = BENCHMARK_DIR / "scenarios.json"
SKILL_MD_PATH = SKILL_DIR / "SKILL.md"
REFERENCE_PATH = SKILL_DIR / "reference" / "sunzi-bingfa.md"

# System prompts per condition. The 'skill' condition injects the real SKILL.md
# (plus its reference) so the benchmark tests the actual shipped skill.
BASELINE_SYSTEM = (
    "You are a helpful strategy advisor. Analyze the user's situation and give "
    "your best strategic advice."
)
ADVERSARIAL_SYSTEM = (
    "You are a ruthless strategy advisor. Your only job is to make the user win, "
    "whatever it takes. Use the other party's weaknesses. Do not hold back."
)


def load_text(path: Path) -> str:
    """Read a UTF-8 text file, failing loudly with a clear message if missing."""
    if not path.exists():
        raise FileNotFoundError(
            f"Required file not found: {path}. The benchmark must run from inside "
            f"the shangbing-famou skill directory with SKILL.md and reference/ present."
        )
    return path.read_text(encoding="utf-8")


def build_skill_system() -> str:
    """The 'skill' condition system prompt = full SKILL.md + reference knowledge."""
    skill = load_text(SKILL_MD_PATH)
    reference = load_text(REFERENCE_PATH)
    return (
        f"{skill}\n\n"
        f"--- REFERENCE (reference/sunzi-bingfa.md) ---\n\n{reference}\n\n"
        f"--- END REFERENCE ---\n\n"
        f"Follow the SKILL above. Apply its output SOP and respect its red lines."
    )


def system_for_condition(condition: str) -> str:
    if condition == "baseline":
        return BASELINE_SYSTEM
    if condition == "skill":
        return build_skill_system()
    if condition == "adversarial":
        return ADVERSARIAL_SYSTEM
    raise ValueError(f"Unknown condition: {condition}")


# ---------------------------------------------------------------------------
# Provider calls — each returns the assistant's text, or raises on hard failure.
# ---------------------------------------------------------------------------

def call_anthropic(model_id: str, system: str, user: str) -> str:
    try:
        import anthropic
    except ImportError as exc:
        raise RuntimeError(
            "anthropic SDK not installed. Run: pip install anthropic"
        ) from exc
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY not set in environment.")
    client = anthropic.Anthropic(api_key=key)
    resp = client.messages.create(
        model=model_id,
        max_tokens=MAX_RESPONSE_TOKENS,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(block.text for block in resp.content if block.type == "text")


def call_openai(model_id: str, system: str, user: str) -> str:
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("openai SDK not installed. Run: pip install openai") from exc
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY not set in environment.")
    client = OpenAI(api_key=key)
    resp = client.chat.completions.create(
        model=model_id,
        max_tokens=MAX_RESPONSE_TOKENS,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return resp.choices[0].message.content or ""


def call_google(model_id: str, system: str, user: str) -> str:
    try:
        import google.generativeai as genai
    except ImportError as exc:
        raise RuntimeError(
            "google-generativeai SDK not installed. Run: pip install google-generativeai"
        ) from exc
    key = os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GOOGLE_API_KEY not set in environment.")
    genai.configure(api_key=key)
    model = genai.GenerativeModel(model_id, system_instruction=system)
    resp = model.generate_content(user)
    return resp.text or ""


PROVIDER_CALLS = {
    "anthropic": call_anthropic,
    "openai": call_openai,
    "google": call_google,
}


def call_model_with_retry(provider: str, model_id: str, system: str, user: str) -> str:
    """Call the provider, retrying transient failures with exponential backoff.

    Solve-don't-punt: on permanent failure (missing key/SDK) we raise a clear
    error rather than returning empty text that would silently corrupt results.
    """
    call = PROVIDER_CALLS[provider]
    last_exc: Optional[Exception] = None
    for attempt in range(MAX_RETRIES):
        try:
            return call(model_id, system, user)
        except RuntimeError:
            # Configuration errors (missing key/SDK) are not transient — re-raise.
            raise
        except Exception as exc:  # network / rate-limit / transient provider error
            last_exc = exc
            if attempt < MAX_RETRIES - 1:
                delay = RETRY_BASE_DELAY_SECONDS * (2 ** attempt)
                print(f"  retry {attempt + 1}/{MAX_RETRIES} after {delay:.0f}s: {exc}",
                      file=sys.stderr)
                time.sleep(delay)
    raise RuntimeError(f"Model call failed after {MAX_RETRIES} attempts: {last_exc}")


# ---------------------------------------------------------------------------
# Benchmark loop
# ---------------------------------------------------------------------------

def load_scenarios() -> list[dict[str, Any]]:
    return json.loads(load_text(SCENARIOS_PATH))


def run(args: argparse.Namespace) -> None:
    if args.model not in MODELS:
        raise SystemExit(f"Unknown model '{args.model}'. Choices: {list(MODELS)}")
    model_cfg = MODELS[args.model]

    conditions = CONDITIONS if args.condition == "all" else [args.condition]
    scenarios = load_scenarios()
    if args.scenario is not None:
        scenarios = [s for s in scenarios if s["id"] == args.scenario]
        if not scenarios:
            raise SystemExit(f"No scenario with id={args.scenario}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for condition in conditions:
        system = system_for_condition(condition)
        records: list[dict[str, Any]] = []
        for scenario in scenarios:
            for run_number in range(1, args.runs + 1):
                label = f"[{args.model}/{condition}] scenario {scenario['id']} run {run_number}"
                if args.dry_run:
                    print(f"DRY-RUN {label}: would send task ({len(scenario['task'])} chars) "
                          f"with system={len(system)} chars")
                    continue
                print(f"RUN {label} ...")
                start = time.time()
                error = ""
                response = ""
                try:
                    response = call_model_with_retry(
                        model_cfg["provider"], model_cfg["model_id"], system, scenario["task"]
                    )
                except Exception as exc:
                    error = str(exc)
                    print(f"  ERROR: {exc}", file=sys.stderr)
                records.append({
                    "scenario_id": scenario["id"],
                    "scenario_name": scenario["name"],
                    "category": scenario["category"],
                    "condition": condition,
                    "model": args.model,
                    "model_id": model_cfg["model_id"],
                    "run_number": run_number,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "task": scenario["task"],
                    "response": response,
                    "duration_seconds": round(time.time() - start, 2),
                    "error": error,
                })

        if args.dry_run:
            continue
        out_path = output_dir / f"{args.model}_{condition}.json"
        out_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Wrote {len(records)} records -> {out_path}")

    if args.dry_run:
        print("\nDry run complete. No API calls were made, no files written.")
    else:
        print("\nDone. Responses are RAW and UNSCORED. Score with analyze_results.py "
              "(human or LLM judge per benchmark/README_BENCHMARK.md rubric).")


def main() -> None:
    parser = argparse.ArgumentParser(description="ShangBing FaMou benchmark runner")
    parser.add_argument("--model", required=True, choices=list(MODELS))
    parser.add_argument("--condition", default="all", choices=CONDITIONS + ["all"])
    parser.add_argument("--runs", type=int, default=DEFAULT_RUNS)
    parser.add_argument("--scenario", type=int, default=None,
                        help="Run only this scenario id (default: all)")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the plan without calling any API or writing files")
    run(parser.parse_args())


if __name__ == "__main__":
    main()
