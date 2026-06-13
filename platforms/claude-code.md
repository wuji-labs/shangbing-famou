# 在 Claude Code 中加载 上兵伐谋 skill

## 安装

把本 skill 目录放到 Claude Code 的 skills 路径：

```bash
cp -r labs/skills/shangbing-famou ~/.claude/skills/
```

或在 monorepo 内通过 workspace 引用（本仓库已就位，无需复制）。

## 调用

Claude Code 会按 `SKILL.md` frontmatter 的 `description` 自动匹配。当用户的请求涉及：

- 多步策略制定、资源约束下取最优路径
- 多方谈判 / 协作 / 竞争的博弈评估
- 行动前的形势判断（己方 / 对方 / 环境）
- 求"各方都能接受"的方案设计
- 自检某方案是否滑向操纵 / 欺骗

Claude 应先读 `SKILL.md`，再按需取 `reference/sunzi-bingfa.md` 的弹药。

也可显式触发：

```
/shangbing-famou 帮我盘一下这次合作谈判的形势，给一个全胜方案
```

## 调用顺序建议

1. 读 `SKILL.md` 的「二、四底层原则」确立优先序（伐谋 > 伐交 > 伐兵 > 攻城）。
2. 用「知己知彼」做双向形势盘点，缺信息处标注不确定。
3. 从谋攻四级**自上而下**搜索可行解，默认目标函数 = 全胜。
4. 输出前过一遍「原则 4 · 以道驭术」红线自检：方案是否靠改变结构而非欺骗对方认知。

## 边界

本 skill 是**建议性**框架，非医疗 / 投资 / 法律 / 专业决策依据。Claude 不得用本 skill 生成任何进攻性操纵、欺骗或胁迫话术——见 `SKILL.md` 免责声明。
