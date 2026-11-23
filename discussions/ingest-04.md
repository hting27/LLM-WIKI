# Ingest 04 討論紀錄 — S4 OpenAI, A practical guide to building agents (2025)

日期：2026-11-23　｜　Wiki 狀態：3 個來源、11 個概念頁

## 1. 這篇的核心主張

1. Agent = 能代替使用者、相當獨立地完成任務的系統；判準是「LLM 是否控制工作流程的執行」。
2. 聊天機器人、單輪 LLM、分類器不是 agent。
3. 三個核心元件：模型、工具、指令。
4. 每個 agent 都有一個 run 迴圈，直到結束條件；先把單一 agent 做到極致，必要才拆多 agent（manager / decentralized）。
5. 防護欄要多層；超過失敗門檻或高風險行動時要交給人。

## 2. 與既有 Wiki 的關係

- **定義第三種說法**：
  - S1：LLM 大腦 + 規劃 + 記憶 + 工具
  - S3：區分 workflow（路徑寫死）與 agent（LLM 自己決定）
  - S4：LLM 控制工作流程執行 + 會選工具 + 在防護欄內 → agent；沒有控制流程的 LLM 應用不是 agent
  - 共同點：**都要求 LLM 使用工具、與外部互動，不只是聊天**。差異在於「多少控制權交給 LLM」。→ 回答 Q4：簡報可以用「控制權光譜」說明。
- **三元件 vs 三元件**：S1 是「規劃、記憶、工具」，S4 是「模型、工具、指令」。兩個都叫「三個核心元件」但內容不同，初學者容易混淆 → 需要在 ai-agent-definition 明確對照。
- **呼應**：S4 的 run 迴圈與結束條件 = agent-loop.md（S2、S3）。
- **新主題**：guardrails 與人工介入，前三篇只零星提到（S3 提沙盒與防護）。
- **多 agent**：前面只有 S3 的 orchestrator-workers；S4 給了 manager / decentralized 兩種模式。

## 3. 提議的頁面變更

| 動作 | 頁面 | 理由 |
|---|---|---|
| 新增 | sources/s4-openai-guide.md | 來源摘要 |
| 新增 | concepts/guardrails-human-oversight.md | 新主題 |
| 新增 | concepts/multi-agent-systems.md | manager / decentralized + orchestrator-workers |
| 修改 | concepts/ai-agent-definition.md | 加 S4 定義、反例、兩種「三元件」對照、控制權光譜 |
| 修改 | concepts/agent-loop.md | 加結束條件清單 |
| 修改 | concepts/tool-use.md | 加工具三分類 |
| 修改 | concepts/when-to-use-agents.md | 加三條件與「規則引擎 vs 調查員」比喻 |
| 修改 | concepts/workflows-vs-agents.md | 補 S4 對照 |

## 4. 待決定的問題

- Q6：要不要寫一頁「名詞表」？術語開始變多（ACI、guardrail、handoff、orchestrator…）。

## 5. 決定

- Q4（定案）：簡報主定義 = 「LLM 自己決定下一步、使用工具、在迴圈中完成任務」，並用控制權光譜（聊天機器人 → workflow → agent）說明。
- Q6：新增 wiki/glossary.md（type: meta），簡報產生時用來檢查術語是否有中文解釋。
- 同意第 3 節變更。
