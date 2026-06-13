# 在 Cursor 中加载 上兵伐谋 skill

## 安装

Cursor 通过 `.cursor/rules/` 下的 `.mdc` 规则文件加载能力。把本 skill 转为一条 rule：

1. 在项目根新建 `.cursor/rules/shangbing-famou.mdc`。
2. 将 `SKILL.md` 的「二、四底层原则」+「三、弹药库导航」摘要写入该 rule 的正文。
3. rule 头部建议设置为按需触发（Agent Requested / 关键词匹配 strategy、negotiation、game theory、博弈、谈判、策略）。

示例 `.mdc` 头：

```mdc
---
description: 上兵伐谋 — winning-without-war strategic reasoning from The Art of War. Apply for multi-step strategy, negotiation, game-theory, and situation-assessment tasks.
globs:
alwaysApply: false
---
```

## 调用

在 Cursor Chat / Composer 中，当任务涉及策略制定、博弈评估、谈判方案、形势判断时，引用本 rule。完整弹药库（《孙子兵法》典源）保留在 `reference/sunzi-bingfa.md`，可在需要原文级精度时让 Cursor 读取该文件。

## 调用顺序建议

1. 谋攻四级优先序：伐谋 > 伐交 > 伐兵 > 攻城，自上而下搜解。
2. 知己知彼：双向形势盘点，缺信息标注不确定。
3. 默认目标函数 = 全胜（保全各方）。
4. 以道驭术红线自检：改变结构而非欺骗对方认知。

## 边界

建议性框架，非医疗 / 投资 / 法律 / 专业决策依据。不得用于生成操纵 / 欺骗 / 胁迫内容。详见 `SKILL.md` 免责声明。
