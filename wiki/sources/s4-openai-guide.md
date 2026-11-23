---
title: "S4 — OpenAI (2025) A practical guide to building agents"
type: source
sources: [S4]
updated: 2026-11-23
---

# S4 — A practical guide to building agents（OpenAI, 2025）

- 原文：https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- 閱讀筆記：`raw/04-openai-2025-practical-guide.md`
- 定位：給產品與工程團隊的實務指南，偏「怎麼做」。

## 一句話摘要

Agent 是能代替使用者、相當獨立地完成任務的系統；由模型、工具、指令組成，先從單一 agent 做起，搭配多層防護欄與人工介入 [S4]。

## 重點

- 定義與反例 → [AI Agent 的定義](../concepts/ai-agent-definition.md)
- run 迴圈與結束條件 → [Agent 迴圈](../concepts/agent-loop.md)
- 工具三分類 → [工具使用](../concepts/tool-use.md)
- 三個適用條件 → [何時該用 Agent](../concepts/when-to-use-agents.md)
- 單 / 多 agent、manager 與 decentralized → [多 Agent 系統](../concepts/multi-agent-systems.md)
- 防護欄與人工介入 → [防護欄與人類監督](../concepts/guardrails-human-oversight.md)

## 其他實務建議

- **模型選擇**：先用最強的模型建立表現基準，再試著換成較小的模型降低成本與延遲 [S4]。
- **指令撰寫**：善用既有作業文件、拆成小步驟、每一步對應明確的動作、預先處理邊界情況 [S4]。
- **結論**：從小做起、用真實使用者驗證、逐步擴充能力 [S4]。
