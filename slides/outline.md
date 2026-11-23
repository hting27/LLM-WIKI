# 簡報大綱：AI Agents 是什麼？

> 依 AGENTS.md §7：先產生大綱、確認後才產生 HTML。
> 產生方式：查詢 `wiki/index.md` → 依「初學者需要先懂什麼」排序概念頁 → 每頁只放一個概念。
> 目標讀者：沒有 AI 背景、但用過 ChatGPT 的大學生。總長約 15–20 分鐘。

## 教學設計

- **起點**：從學生熟悉的 ChatGPT 出發（已知 → 未知）。
- **主軸**：一個「思考 → 行動 → 觀察」迴圈圖，從第 6 頁開始反覆出現，後面每個元件都標示它在迴圈中的位置。
- **避免誤解**：第 12 頁多 agent 的數字一定同時呈現「好處 + 代價 + 不適用情況」（ingest-05 決定 Q7）。
- **術語**：第一次出現的英文術語用 `<abbr title="中文解釋">` 標示（以 wiki/glossary.md 為準）。

## 逐頁大綱

| # | 標題 | 要講的一個概念 | 依據的 wiki 頁面 |
|---|---|---|---|
| 1 | AI Agents 是什麼？ | 封面 | — |
| 2 | 你用過的 ChatGPT 是 agent 嗎？ | 單純聊天機器人不算 agent | concepts/ai-agent-definition.md |
| 3 | 一句話定義 | 會自己決定下一步 + 用工具 + 迴圈；控制權光譜 | concepts/ai-agent-definition.md |
| 4 | 食譜 vs 廚師 | Workflow 與 agent 的差別 | concepts/workflows-vs-agents.md |
| 5 | Agent 的構造 | LLM 大腦 + 規劃 / 記憶 / 工具（＋兩種「三元件」別搞混） | concepts/ai-agent-definition.md, concepts/augmented-llm.md |
| 6 | 核心：Agent 迴圈 | 思考 → 行動 → 觀察；停止條件 | concepts/agent-loop.md |
| 7 | 一個迴圈實例：ReAct | Thought / Action / Observation 範例；34% / 10% | concepts/react.md |
| 8 | 規劃 | 拆解任務、自我反思 | concepts/planning.md |
| 9 | 記憶 | 短期 ≈ context、長期 ≈ 外部資料庫 | concepts/memory.md |
| 10 | 工具 | 三類工具；ACI 絕對路徑案例 | concepts/tool-use.md |
| 11 | 五種常見組合方式 | workflow 模式概覽表 | concepts/workflow-patterns.md |
| 12 | 一個不夠，那就多個？ | 多 agent：90.2% 好處 vs 15 倍成本 vs 不適用情況 | concepts/multi-agent-systems.md |
| 13 | 什麼時候該用 agent？ | 先簡單；S4 三條件 | concepts/when-to-use-agents.md |
| 14 | 風險與防護欄 | 錯誤累積；多層防護；兩個交給人的時機 | concepts/challenges-and-risks.md, concepts/guardrails-human-oversight.md |
| 15 | 怎麼知道 agent 做得好不好？ | 小樣本、LLM 評審、人工評估 | concepts/evaluation.md |
| 16 | 小測驗 | 回顧（三題） | concepts/ai-agent-definition.md, concepts/agent-loop.md, concepts/when-to-use-agents.md |
| 17 | 參考資料 | 五篇來源 | sources/*.md |

## 刻意不放進簡報的 wiki 內容（及理由）

- MIPS / ANN 演算法、Chain of Hindsight、LLM+P：對初學者太深。
- S4 的 manager / decentralized 細節：只在第 12 頁口頭帶過，不另開一頁。
- S5 的部署細節（rainbow deployment）：屬於工程實務，非基本概念。

## 確認

- [x] 每頁只有一個概念
- [x] 每頁都對應到至少一個 wiki 頁面
- [x] 數字只用 wiki 中有的（將由 check_slides.py 驗證）
- 決定：通過，進入 HTML 產生。
