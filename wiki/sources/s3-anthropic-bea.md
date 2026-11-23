---
title: "S3 — Anthropic (2024) Building effective agents"
type: source
sources: [S3]
updated: 2026-11-23
---

# S3 — Building effective agents（Anthropic, 2024）

- 原文：https://www.anthropic.com/research/building-effective-agents
- 閱讀筆記：`raw/03-anthropic-2024-building-effective-agents.md`
- 定位：業界實務指南，提出 workflow / agent 區分與五種常見模式。
- 註：網頁在 2026 年加註部分工具生態已改變，但文中的模式仍被廣泛引用 [S3]。

## 一句話摘要

最成功的 agent 系統通常是用簡單、可組合的模式打造，而不是複雜框架；能不用 agent 就不用 [S3]。

## 重點

- Workflow 與 agent 的區分 → [Workflows vs Agents](../concepts/workflows-vs-agents.md)
- 基本積木 → [Augmented LLM](../concepts/augmented-llm.md)
- 五種模式 → [Workflow 模式](../concepts/workflow-patterns.md)
- 何時用 / 不用 → [何時該用 Agent](../concepts/when-to-use-agents.md)
- 迴圈中依環境回饋用工具 → [Agent 迴圈](../concepts/agent-loop.md)
- ACI 與工具設計 → [工具使用](../concepts/tool-use.md)
- 成本與錯誤累積 → [挑戰與風險](../concepts/challenges-and-risks.md)

## 實務案例

- **客服**：對話 + 需要查資料與執行動作（退款、更新工單），成功與否容易衡量 [S3]。
- **程式碼 agent**：可以用自動化測試驗證並依測試結果迭代；但仍需要人審查是否符合整體需求 [S3]。
