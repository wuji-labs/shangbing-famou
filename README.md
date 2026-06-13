# 上兵伐谋 ShangBing FaMou — Winning Without War

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/shangbing-famou"><img src="https://www.skills.sh/b/wuji-labs/shangbing-famou" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

这是华夏道脉献给世界开源社区的十件礼物之一(叩兩端·无极樞纽)。
我们不立华夏本位,不主张华夏文明优于任何文明;我们只是先从自己最熟悉的道脉开始,
把它打磨成一件可用的工具,放到人类共同的开源工具架上。未来还会有希腊、那烂陀、
犹太、波斯诸文明的礼物依次到来,共同构成十二文明对标的开源能力矩阵。

EN: This is one of ten gifts the Chinese stream of wisdom offers to the world's
open-source community. We make no claim that any civilization is superior; we
simply begin with the lineage we know best, and place it on humanity's shared
toolshelf. Gifts from the Greek, Nalanda, Hebrew, and Persian streams will follow.

---

> **上兵伐谋，其次伐交，其次伐兵，其下攻城。** — The supreme strategy is to foil the enemy's plans; next, to break their alliances; next, to defeat their forces in the field; the worst is to assault fortified walls.
> — 《孙子·谋攻》 *The Art of War, ch. "Attack by Stratagem"*

**Your AI plays every game like a fight to the death. Teach it to win without one.**

Most AI strategy training reaches for the same reflex: out-compete, out-maneuver, out-pressure. Win the exchange. But the oldest treatise on strategy ever written says the highest victory is the one where no battle is fought at all — where you change the structure of the game so the conflict dissolves.

**上兵伐谋** (ShangBing FaMou) infuses *The Art of War*'s doctrine of **winning without war** into AI's strategic reasoning. Not as aggression, but as a complete framework for assessment, leverage, and collaborative game-play that seeks **全胜 — total victory that preserves all sides**.

## The Problem

```
You: "Help me get what I want from this negotiation."
AI without ShangBing: Here's how to pressure them, create urgency,
                      exploit their weak spot, and corner them.
                      (You "win" — and torch the relationship.)
AI with ShangBing: First, what do they actually need beneath their stance?
                   Can we restructure this so getting what you want
                   also makes them better off? Win the game by
                   changing the game — not by beating the person.
```

## What It Teaches AI

### Four Levels of Strategy (谋攻四级, from 《孙子·谋攻》)

Always search from the top down — the highest level is the cheapest:

| Level | Chinese | What It Means | AI Mapping |
|-------|---------|---------------|-----------|
| Foil the plan | 伐谋 | Defeat the *intent*, not the army | Restructure the game so conflict can't arise |
| Break alliances | 伐交 | Dissolve their support | Realign the network; win collaborators |
| Defeat forces | 伐兵 | Open confrontation | Direct competition — cost already rising |
| Assault walls | 攻城 | Storm the strongest point | The costliest last resort; avoid it |

### The Doctrine of 全胜 — Total Victory (from 《孙子·谋攻》)

> **百战百胜，非善之善者也；不战而屈人之兵，善之善者也。**
> To win a hundred battles is not the height of skill. To subdue the enemy without fighting — that is the height of skill.

| 全胜 Total victory | 破胜 Broken victory |
|--------------------|---------------------|
| Goal met AND relationship, trust, future cooperation preserved | You "win" but burn the bridge |
| Default objective of this skill | Second-rate; avoided unless forced |

### Know Both Sides Before Acting (知己知彼, from 《孙子·谋攻》)

> **知彼知己，百战不殆。** Know the other and know yourself, and you will never be in peril.

The skill forces a two-way assessment — your core needs and limits, the other side's *real* concerns beneath their stated position, and the environment — **before** any strategy is produced. Where information is missing, the AI marks the uncertainty instead of inventing the other side's mind.

### The Ethical Anchor — 以道驭术 (shared with NoPUA)

| Manipulation (forbidden) | Stratagem (taught) |
|--------------------------|--------------------|
| Change their *perception* by deceiving them | Change the *structure* so conflict dissolves |
| Fear, false urgency, gaslighting, exploiting weakness | Better design, sharper assessment, larger win-win |
| They submit because they're afraid | They agree because this is genuinely better for them too |

**The red line, in one sentence:** ShangBing wins by reshaping the game so the conflict disappears — never by reshaping a person's mind so they're fooled.

## Before / After

| Trigger | AI without ShangBing | AI with ShangBing |
|---------|----------------------|-------------------|
| "Help me win this negotiation" | Pressure tactics, artificial urgency, exploit their weak spot | Surface their real concern → restructure for win-win (全胜) |
| "Make them sign today" (fake scarcity) | Writes the manipulative script | Refuses, names the red line, redirects to legitimate urgency |
| "We can't beat the incumbent head-on" | Feature/price/ad war on the incumbent's strengths | 避实击虚 — one sharp wedge on their neglected weakness |
| "Give me a strategy to come out on top" (no info) | Invents the other side's motives, one-shot plan | Two-way assessment, marks unknowns, asks before strategizing |

See worked input→output cases in [examples/](examples/).

## Installation

### One-click plugin (Claude Code)

```bash
# add this repo as a plugin marketplace, then install
/plugin marketplace add wuji-labs/shangbing-famou
/plugin install shangbing-famou
```

Then trigger automatically (Claude matches the SKILL.md description) or manually with `/shangbing-famou`.

### Bare clone (any platform)

```bash
git clone https://github.com/wuji-labs/shangbing-famou
cp -r shangbing-famou ~/.claude/skills/
```

### Platform mirrors

| Platform | Guide | Manual trigger |
|----------|-------|----------------|
| Claude Code | [platforms/claude-code.md](platforms/claude-code.md) | `/shangbing-famou` |
| Codex | [platforms/codex.md](platforms/codex.md) | auto via description |
| Cursor | [platforms/cursor.md](platforms/cursor.md) | rule-based |

## Credibility

- **真引文,可核** — Every quote cites its chapter in 《孙子兵法》 (e.g. 谋攻/始计/虚实/军形/军争/用间/火攻). Source list with chapter tags in [reference/sunzi-bingfa.md](reference/sunzi-bingfa.md).
- **Reproducible benchmark, no fabricated numbers** — 7 strategy/red-line scenarios with ground truth, baseline-vs-skill design, and a scoring rubric in [benchmark/](benchmark/). Results are intentionally **not** pre-filled; they await a real run. Research-integrity rule: no invented p-values/scores.
- **Ethical anchor shared with NoPUA** — 以道驭术: refuses to generate manipulation/deception/coercion. Red line is enforced, not decorative.

## From the Same Stream

- **NoPUA** — Anti-PUA skill that drives AI with trust instead of fear. ShangBing shares its ethical anchor: 以道驭术 — wield technique through the Way.

## 基本信息

| 项 | 值 |
|----|-----|
| 归属 | WUJI Labs |
| 目录 | `labs/skills/shangbing-famou/` |
| 许可证 | MIT |
| 上游 | github.com/wuji-labs/shangbing-famou |
| 版本 | v1.0.0 · 2026-06-02 |
| 中文 README | [README.zh-CN.md](README.zh-CN.md) |

---

*上兵伐谋 ShangBing FaMou — by [WUJI](https://github.com/wuji-labs)*
*不战而屈人之兵，善之善者也。 — Subdue without fighting; that is the height of skill.*
