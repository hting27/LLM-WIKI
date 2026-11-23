---
title: "S5 — Anthropic (2025) How we built our multi-agent research system"
type: source
sources: [S5]
updated: 2026-11-23
---

# S5 — How we built our multi-agent research system（Anthropic, 2025）

- 原文：https://www.anthropic.com/engineering/multi-agent-research-system
- 閱讀筆記：`raw/05-anthropic-2025-multi-agent-research.md`
- 定位：真實產品（Claude 的 Research 功能）的工程案例，補上「評估」與「上線」的實務。

## 一句話摘要

研究型任務無法事先寫死步驟，適合用「主 agent 規劃 + 平行子 agent 搜尋」的多 agent 架構；效果明顯更好，但 token 成本也高很多 [S5]。

## 重點

- 架構、數據、適用條件 → [多 Agent 系統](../concepts/multi-agent-systems.md)
- 實際案例對應 orchestrator-workers → [Workflow 模式](../concepts/workflow-patterns.md)
- 小樣本、LLM-as-judge、人工評估 → [評估](../concepts/evaluation.md)
- 把計畫存到外部記憶 → [記憶](../concepts/memory.md)
- 工具說明改善 → [工具使用](../concepts/tool-use.md)
- 上線挑戰 → [挑戰與風險](../concepts/challenges-and-risks.md)

## 早期失敗（教學上很有用的例子）

簡單問題卻開了 50 個子 agent、無止盡地搜尋不存在的資料、子 agent 互相用過多的更新干擾彼此、多個子 agent 重複做同一件事 [S5]。

## 八條提示工程原則（改寫）

站在 agent 角度模擬觀察；教主 agent 怎麼委派；依問題難度決定投入多少；重視工具設計與選擇；讓 agent 改進自己；先廣後窄的搜尋；引導思考過程；平行呼叫工具 [S5]。
