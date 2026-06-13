# 在 Codex 中加载 上兵伐谋 skill

## 安装

把本 skill 目录放到 Codex 的 skills 路径：

```bash
cp -r labs/skills/shangbing-famou ~/.codex/skills/
```

## 调用

Codex 通过 `SKILL.md` 的 frontmatter `name: shangbing-famou` 与 `description` 识别本 skill。在策略 / 博弈 / 谈判 / 形势判断类任务中，先加载 `SKILL.md`，再按需读取 `reference/sunzi-bingfa.md`。

显式引用（在 prompt 中）：

```
载入 skill: shangbing-famou
任务：在以下约束下给出一个最省力且各方可接受的策略路径……
```

## 在 app-server 长连接下的用法

集团 bot 默认 codex app-server 长连接（ADR-0008）。本 skill 为纯文本知识层，无构建产物（`package.json` 的 `build` / `clean` 均为 echo 占位），可直接随会话上下文加载，不依赖运行时服务。

## 调用顺序建议

1. 先读「四底层原则」，锁定谋攻四级优先序与全胜目标函数。
2. 做「知己知彼」双向盘点，不确定处显式标注。
3. 自上而下搜可行解（伐谋 → 伐交 → 伐兵 → 攻城）。
4. 红线自检（以道驭术）：拒绝任何操纵 / 欺骗 / 胁迫输出。

## 边界

建议性内容，非专业决策依据。详见 `SKILL.md` 免责声明。
