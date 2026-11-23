---
title: 名詞表
type: meta
sources: [S1, S2, S3, S4]
updated: 2026-11-23
---

# 名詞表（給初學者）

> 簡報規則：第一次出現的英文術語要附中文解釋，解釋以本表為準。

| 術語 | 中文 / 白話解釋 | 詳見 |
|---|---|---|
| LLM | 大型語言模型，例如 ChatGPT、Claude 背後的模型 | — |
| Agent | 能自己決定下一步、使用工具、在迴圈中完成任務的 AI 系統 | [定義](concepts/ai-agent-definition.md) |
| Agentic system | 所有「LLM + 工具」系統的統稱，包含 workflow 與 agent [S3] | [Workflows vs Agents](concepts/workflows-vs-agents.md) |
| Workflow | 流程由程式預先寫好的 LLM 系統 [S3] | [Workflows vs Agents](concepts/workflows-vs-agents.md) |
| Tool / Tool use | 工具 / 工具使用：讓 LLM 呼叫搜尋、計算、資料庫等外部功能 | [工具使用](concepts/tool-use.md) |
| API | 程式之間互相呼叫的介面 | — |
| Context window | 上下文視窗：模型一次能「看到」的文字量，相當於短期記憶 [S1] | [記憶](concepts/memory.md) |
| Token | 模型處理文字的最小單位，大約是一個字或半個字；用量決定成本 | — |
| Embedding / 向量 | 把文字轉成一串數字，方便比較意思相不相近 [S1] | [記憶](concepts/memory.md) |
| Chain of Thought | 思維鏈：讓模型一步一步寫出推理 [S1] | [規劃](concepts/planning.md) |
| ReAct | 推理（Reason）與行動（Act）交錯進行的方法 [S2] | [ReAct](concepts/react.md) |
| Hallucination | 幻覺：模型講出看似合理但錯誤的內容 | [挑戰與風險](concepts/challenges-and-risks.md) |
| ACI | Agent-computer interface：給 agent 用的工具介面設計 [S3] | [工具使用](concepts/tool-use.md) |
| Orchestrator | 指揮者：負責拆任務、分派、整合的中央 agent [S3] | [多 Agent](concepts/multi-agent-systems.md) |
| Handoff | 交接：一個 agent 把工作轉給另一個 agent [S4] | [多 Agent](concepts/multi-agent-systems.md) |
| Guardrail | 防護欄：限制 agent 行為、過濾危險輸入輸出的機制 [S4] | [防護欄](concepts/guardrails-human-oversight.md) |
| Prompt injection | 提示注入：在輸入裡藏指令，企圖讓 AI 做原本不該做的事 [S4] | [防護欄](concepts/guardrails-human-oversight.md) |
| Human-in-the-loop | 人在迴圈中：關鍵步驟由人確認 | [防護欄](concepts/guardrails-human-oversight.md) |
