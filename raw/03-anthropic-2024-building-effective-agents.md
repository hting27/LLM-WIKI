# S3 — Building effective agents

- 作者：Erik Schluntz、Barry Zhang（Anthropic Engineering）
- 日期：2024-12-19（網頁於 2026 年加註：部分工具生態已改變，但模式本身仍適用）
- 網址：https://www.anthropic.com/research/building-effective-agents
- 類型：業界實務指南
- 取得方式：網頁全文閱讀（2026-11-23）
- 版權說明：本檔只存放閱讀筆記（自行改寫）。

## 閱讀筆記（改寫）

- 觀察：和數十個團隊合作後，最成功的做法通常不是用複雜框架，而是**簡單、可組合的模式**。
- 定義：把所有變體統稱為 **agentic systems**，再分成兩種：
  - **Workflows（工作流）**：LLM 和工具依「預先寫好的程式路徑」被編排。
  - **Agents（代理）**：LLM 自己動態決定流程與要用哪些工具，掌控完成任務的方式。
- 何時用：先找最簡單的解法，必要時才加複雜度；很多應用只要優化單次 LLM 呼叫（加檢索、加範例）就夠。Agentic 系統通常用「延遲與成本」換「表現」。
- 框架：可以加速起步，但多一層抽象會讓除錯變難；建議先直接用 API。
- 基本積木：**Augmented LLM** —— LLM + 檢索 + 工具 + 記憶。
- 五種 workflow 模式：
  1. Prompt chaining（提示鏈）：拆成固定步驟，可在中間加程式檢查（gate）。
  2. Routing（路由）：先分類輸入，再送到專門處理流程。
  3. Parallelization（平行化）：sectioning（拆成獨立子任務同時做）或 voting（同一任務做多次取多數）。
  4. Orchestrator-workers（指揮者-工人）：中央 LLM 動態拆任務、分派、整合；子任務事先無法預測。
  5. Evaluator-optimizer（評估者-優化者）：一個產生、一個評估回饋，迴圈改進；適用於有清楚評估標準時。
- Agents：本質上通常只是「LLM 在迴圈中根據環境回饋使用工具」。每一步要從環境拿到 ground truth（例如工具結果、程式執行結果）評估進度；可在檢查點暫停等人回饋；常設停止條件（例如最大迭代次數）。
- 風險：成本較高、錯誤可能累積（compounding errors）→ 建議在沙盒中大量測試並加防護。
- 三原則：保持**簡單**、讓規劃步驟**透明**、用心設計 **ACI（agent-computer interface）**——工具文件與測試。
- 實務案例：客服、程式碼 agent（可用自動化測試驗證，但仍需人審查）。
- 工具設計：把工具定義當作提示工程來做；格式要接近模型在網路上常見的格式；用防呆（poka-yoke）設計參數。例：SWE-bench agent 改成強制使用絕對路徑後，模型就不再出錯；他們花在優化工具的時間比優化整體提示還多。

## 我的初步判斷

- 與 S1 的定義有差異：S1 把「LLM + 規劃/記憶/工具」都叫 agent；S3 把「預先寫好路徑」的系統另外叫 workflow。需要在 wiki 裡處理這個差異。
