# Ingest 03 討論紀錄 — S3 Anthropic, Building effective agents (2024)

日期：2026-11-23　｜　Wiki 狀態：2 個來源、7 個概念頁

## 1. 這篇的核心主張

1. 「agentic systems」分兩種：**workflow**（路徑由程式預先寫好）與 **agent**（LLM 自己決定流程與工具）。
2. 先用最簡單的方案；agentic 系統用延遲與成本換表現。
3. 基本積木是 augmented LLM（LLM + 檢索 + 工具 + 記憶）。
4. 五種常見 workflow 模式：prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer。
5. Agent 通常就是「LLM 在迴圈中依環境回饋使用工具」；三原則：簡單、透明、好好設計 ACI。

## 2. 與既有 Wiki 的關係

- **衝突（重要）**：ai-agent-definition.md 目前只有 S1 的定義（LLM + 規劃/記憶/工具 = agent）。依 S3，很多「有工具、有規劃」但路徑寫死的系統應該叫 workflow，不叫 agent。這會影響簡報最核心的那一頁。
- **呼應**：S3 的 agent 描述（迴圈中依環境回饋用工具、每步拿 ground truth）與 agent-loop.md（S2）一致 → 可以把 S3 加為 agent-loop 的第二個來源。
- **呼應**：S3 的 augmented LLM ≈ S1 的三元件，但 S3 把它定位成「積木」，不是 agent 本身。
- **補充**：「何時不要用 agent」是前兩篇完全沒有的觀點，對初學者很重要（避免以為 agent 一定比較好）。
- **補充**：ACI / 工具設計可以擴充 tool-use.md。

## 3. 提議的頁面變更

| 動作 | 頁面 | 理由 |
|---|---|---|
| 新增 | sources/s3-anthropic-bea.md | 來源摘要 |
| 新增 | concepts/workflows-vs-agents.md | 核心區分，獨立成頁 |
| 新增 | concepts/augmented-llm.md | 積木概念 |
| 新增 | concepts/workflow-patterns.md | 五種模式 |
| 新增 | concepts/when-to-use-agents.md | 何時用 / 不用 |
| 修改 | concepts/ai-agent-definition.md | 加入 S3 定義 + `## 觀點差異` |
| 修改 | concepts/agent-loop.md | 加 S3 為來源；補停止條件、人類檢查點 |
| 修改 | concepts/tool-use.md | 加 ACI 與工具設計建議 |
| 修改 | concepts/challenges-and-risks.md | 加成本與錯誤累積 |

## 4. 待決定的問題

- Q4：簡報要採用哪個定義當「主定義」？
- Q5：五種 workflow 模式全部放進簡報嗎？

## 5. 決定

- Q4：wiki 兩種定義都保留；簡報先用「廣義：LLM + 工具 + 迴圈」讓初學者建立直覺，再用一頁說明 S3 的 workflow / agent 區分。待 S4 ingest 後再確認。
- Q5：wiki 全部收錄；簡報只用一頁表格概覽，不逐一講解（初學者負擔太大）。
- 同意第 3 節變更。
