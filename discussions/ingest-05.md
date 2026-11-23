# Ingest 05 討論紀錄 — S5 Anthropic, multi-agent research system (2025)

日期：2026-11-23　｜　Wiki 狀態：4 個來源、13 個概念頁 + glossary

## 1. 這篇的核心主張

1. 研究型任務無法事先寫死步驟 → 適合 agent。
2. Orchestrator-worker 架構：主 agent 規劃並平行派出子 agent，最後由引用 agent 標來源。
3. 多 agent 在內部研究評測比單 agent 好 90.2%，但 token 約是聊天的 15 倍（單 agent 約 4 倍）。
4. 需要共享 context 或高度相依的任務（如多數寫程式）不適合多 agent。
5. 評估：立刻用約 20 題小樣本開始；LLM-as-judge 量表；人工評估不可少。

## 2. 與既有 Wiki 的關係

- **看似衝突**：S4 說「先把單一 agent 做到極致」；S5 說多 agent 大幅提升表現。
  - 判斷：其實不矛盾，是**條件不同**。S5 自己也說只適合「可平行、資訊量超過單一 context、價值高到值得付 token 成本」的任務。→ 在 multi-agent-systems.md 用 `## 觀點差異` 說清楚條件。
- **呼應**：S5 的架構就是 S3 的 orchestrator-workers 模式的實際案例 → workflow-patterns.md 加連結。
- **呼應**：「把計畫存到記憶以免 context 截斷」呼應 S1 的記憶 / context 限制挑戰。
- **呼應**：工具說明改善 → 任務時間少 40%，支持 S3 的 ACI 觀點。
- **新主題**：評估（evaluation），前四篇幾乎沒有 → 新頁。
- **與 S1 呼應**：S1 的 ChemCrow 指出 LLM 自評在專業領域不可靠；S5 則說 LLM-as-judge 可以規模化、但仍需人工評估。兩者可以放在一起提醒「自動評估的限制」。

## 3. 提議的頁面變更

| 動作 | 頁面 | 理由 |
|---|---|---|
| 新增 | sources/s5-anthropic-multi-agent.md | 來源摘要 |
| 新增 | concepts/evaluation.md | 新主題，含 S1 ChemCrow 對照 |
| 修改 | concepts/multi-agent-systems.md | 加案例、數據、觀點差異 |
| 修改 | concepts/workflow-patterns.md | orchestrator-workers 連到實例 |
| 修改 | concepts/memory.md | 加「外部記憶保存計畫」 |
| 修改 | concepts/tool-use.md | 加 40% 數據 |
| 修改 | concepts/challenges-and-risks.md | 加正式上線挑戰 |
| 修改 | concepts/when-to-use-agents.md | 加多 agent 的適用條件 |

## 4. 待決定的問題

- Q7：90.2%、15 倍這類數字要放進簡報嗎？初學者可能誤以為「多 agent 一定好」。

## 5. 決定

- Q7：放，但同一頁必須同時呈現「好處（90.2%）」與「代價（15 倍 token）」與「不適用情況」，避免片面。
- 同意第 3 節變更。完成本輪後執行 lint，通過後進入簡報階段。
