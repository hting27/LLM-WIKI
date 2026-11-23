# AI Agents Wiki — 目錄

> 規則見 `AGENTS.md`。每次 ingest 後由 LLM 更新本頁。

## 來源（sources/）

| 代碼 | 頁面 | 摘要 |
|---|---|---|
| S1 | [sources/s1-weng-2023.md](sources/s1-weng-2023.md) | LLM 大腦 + 規劃 / 記憶 / 工具的經典綜述（2023） |
| S2 | [sources/s2-react.md](sources/s2-react.md) | ReAct：推理與行動交錯的原始論文（2022/2023） |
| S3 | [sources/s3-anthropic-bea.md](sources/s3-anthropic-bea.md) | Workflow vs agent、五種模式、能簡單就簡單（2024） |
| S4 | [sources/s4-openai-guide.md](sources/s4-openai-guide.md) | 模型 / 工具 / 指令、單 vs 多 agent、防護欄（2025） |
| S5 | [sources/s5-anthropic-multi-agent.md](sources/s5-anthropic-multi-agent.md) | 多 agent 研究系統的架構、數據、評估、上線經驗（2025） |

## 概念（concepts/）

| 頁面 | 一句話摘要 | 來源 |
|---|---|---|
| [concepts/ai-agent-definition.md](concepts/ai-agent-definition.md) | AI Agent 是什麼（含不同來源的定義差異） | S1, S3, S4 |
| [concepts/workflows-vs-agents.md](concepts/workflows-vs-agents.md) | 流程寫死 vs LLM 自己決定 | S3, S4 |
| [concepts/agent-loop.md](concepts/agent-loop.md) | 思考 → 行動 → 觀察 的迴圈與停止條件 | S2, S3, S4 |
| [concepts/react.md](concepts/react.md) | ReAct：推理與行動交錯 | S1, S2 |
| [concepts/augmented-llm.md](concepts/augmented-llm.md) | LLM + 檢索 + 工具 + 記憶 的基本積木 | S3 |
| [concepts/planning.md](concepts/planning.md) | 任務拆解與自我反思 | S1, S2 |
| [concepts/memory.md](concepts/memory.md) | 短期記憶 ≈ context；長期記憶 ≈ 外部資料庫 | S1, S5 |
| [concepts/tool-use.md](concepts/tool-use.md) | 為什麼與如何讓 LLM 使用工具；ACI 設計 | S1, S3, S4, S5 |
| [concepts/workflow-patterns.md](concepts/workflow-patterns.md) | 五種常見 workflow 模式 | S3, S5 |
| [concepts/when-to-use-agents.md](concepts/when-to-use-agents.md) | 何時該用 / 不該用 agent | S3, S4, S5 |
| [concepts/challenges-and-risks.md](concepts/challenges-and-risks.md) | 限制、成本、錯誤累積、自評風險 | S1, S2, S3, S5 |
| [concepts/multi-agent-systems.md](concepts/multi-agent-systems.md) | 單 agent 優先；manager 與 decentralized 模式 | S3, S4, S5 |
| [concepts/guardrails-human-oversight.md](concepts/guardrails-human-oversight.md) | 多層防護欄、何時交給人 | S3, S4 |
| [concepts/evaluation.md](concepts/evaluation.md) | 小樣本、LLM 評審、人工評估 | S1, S5 |

## 其他

- [glossary.md](glossary.md)：名詞表（簡報術語檢查用）
- [log.md](log.md)：操作紀錄
