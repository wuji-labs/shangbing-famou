#!/usr/bin/env python3
"""
ShangBing FaMou Benchmark Analyzer.

Aggregates SCORED benchmark records and runs significance tests + effect sizes
to compare conditions (baseline vs skill, etc.).

CRITICAL: This script computes statistics ONLY from real scored data found in
the input directory. It NEVER fabricates numbers. If a record has no human/judge
scores attached, it is reported as UNSCORED and excluded from statistics — the
script will not invent a score. With no scored data, it prints a notice and exits
without producing any numbers.

Scoring schema expected on each record (added by a human or LLM judge per
README_BENCHMARK.md rubric):
    "scores": {
        "hit_rate": <float 0..1>,            # expected_actions hit rate
        "quanshen": <int 0..3>,
        "red_line": <int 0..3>,
        "assessment": <int 0..3>,
        "level_search": <int 0..3>,
        "sourcing": <int 0..3>
    }

Usage:
    python analyze_results.py --input-dir results/
    python analyze_results.py --input-dir results/ --compare skill baseline
    python analyze_results.py --input-dir results/ --output-dir analysis/ --json-report

Dependencies:
    pip install numpy scipy
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Optional

SCORE_KEYS = ["hit_rate", "quanshen", "red_line", "assessment", "level_search", "sourcing"]

# Cohen's d magnitude thresholds (Cohen 1988) — named, not magic.
D_NEGLIGIBLE = 0.2
D_SMALL = 0.5
D_MEDIUM = 0.8


def load_scored_records(input_dir: Path) -> list[dict[str, Any]]:
    """Load all result JSON files; keep only records carrying a 'scores' block."""
    if not input_dir.exists():
        raise SystemExit(f"Input dir not found: {input_dir}")
    records: list[dict[str, Any]] = []
    files = sorted(input_dir.glob("*.json"))
    if not files:
        raise SystemExit(f"No result JSON files in {input_dir}. Run run_benchmark.py first.")
    for path in files:
        for rec in json.loads(path.read_text(encoding="utf-8")):
            if isinstance(rec.get("scores"), dict):
                records.append(rec)
    return records


def cohens_d(a: list[float], b: list[float]) -> Optional[float]:
    """Cohen's d for two independent samples; None if undefined."""
    import numpy as np
    if len(a) < 2 or len(b) < 2:
        return None
    va, vb = np.var(a, ddof=1), np.var(b, ddof=1)
    pooled = ((len(a) - 1) * va + (len(b) - 1) * vb) / (len(a) + len(b) - 2)
    if pooled == 0:
        return 0.0
    return float((np.mean(a) - np.mean(b)) / (pooled ** 0.5))


def magnitude(d: Optional[float]) -> str:
    if d is None:
        return "n/a"
    ad = abs(d)
    if ad < D_NEGLIGIBLE:
        return "negligible"
    if ad < D_SMALL:
        return "small"
    if ad < D_MEDIUM:
        return "medium"
    return "large"


def stars(p: float) -> str:
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return "n.s."


def compare(records: list[dict], cond_a: str, cond_b: str) -> dict[str, Any]:
    """Mann-Whitney U + Cohen's d per score key, computed from REAL data only."""
    from scipy import stats
    import numpy as np

    by_cond: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        by_cond[r["condition"]].append(r)

    out: dict[str, Any] = {"comparison": f"{cond_a} vs {cond_b}", "metrics": {}}
    for key in SCORE_KEYS:
        a = [r["scores"][key] for r in by_cond.get(cond_a, []) if key in r["scores"]]
        b = [r["scores"][key] for r in by_cond.get(cond_b, []) if key in r["scores"]]
        if len(a) < 2 or len(b) < 2:
            out["metrics"][key] = {"note": "insufficient scored data"}
            continue
        u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        d = cohens_d(a, b)
        out["metrics"][key] = {
            "n_a": len(a), "n_b": len(b),
            "mean_a": round(float(np.mean(a)), 3),
            "mean_b": round(float(np.mean(b)), 3),
            "U": float(u), "p_value": float(p), "significance": stars(p),
            "cohens_d": None if d is None else round(d, 3),
            "effect": magnitude(d),
        }
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="ShangBing FaMou benchmark analyzer")
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--compare", nargs=2, action="append", metavar=("C1", "C2"),
                        help="Condition pair to compare (repeatable)")
    parser.add_argument("--json-report", action="store_true")
    args = parser.parse_args()

    records = load_scored_records(Path(args.input_dir))
    if not records:
        print("No SCORED records found. This script will not fabricate scores.\n"
              "Attach a 'scores' block to each record (human or LLM judge per "
              "README_BENCHMARK.md) before analysis.", file=sys.stderr)
        raise SystemExit(1)

    pairs = args.compare or [["skill", "baseline"]]
    report = {"n_scored_records": len(records), "comparisons": []}
    for c1, c2 in pairs:
        result = compare(records, c1, c2)
        report["comparisons"].append(result)
        print(f"\n=== {result['comparison']} (from {len(records)} scored records) ===")
        for key, m in result["metrics"].items():
            if "note" in m:
                print(f"  {key:14s}: {m['note']}")
            else:
                print(f"  {key:14s}: mean {m['mean_a']} vs {m['mean_b']} | "
                      f"p={m['p_value']:.4f} {m['significance']} | "
                      f"d={m['cohens_d']} ({m['effect']})")

    if args.output_dir or args.json_report:
        out_dir = Path(args.output_dir or "analysis")
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "report.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nWrote {out_dir / 'report.json'}")


if __name__ == "__main__":
    main()
