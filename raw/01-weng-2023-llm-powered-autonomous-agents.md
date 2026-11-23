# S1 — LLM Powered Autonomous Agents

- 作者：Lilian Weng（Lil'Log 部落格）
- 日期：2023-06-23
- 網址：https://lilianweng.github.io/posts/2023-06-23-agent/
- 類型：技術綜述文章（入門 + 文獻整理）
- 取得方式：網頁全文閱讀（2026-11-23）
- 版權說明：本檔只存放閱讀筆記（自行改寫），不複製原文段落。

## 閱讀筆記（改寫）

- 文章的核心框架：把 LLM 當成 agent 的「大腦」，再加上三個元件：**規劃（Planning）**、**記憶（Memory）**、**工具使用（Tool use）**。
- 規劃分兩部分：
  - 任務拆解：Chain of Thought（一步一步想）、Tree of Thoughts（每一步考慮多種可能，形成樹狀搜尋）、LLM+P（把規劃外包給傳統規劃器，用 PDDL 當中介語言）。拆解可以靠提示、靠任務專屬指令，或靠人提供。
  - 自我反思：ReAct（思考與行動交錯）、Reflexion（失敗後寫反思存進工作記憶，最多三則）、Chain of Hindsight（把過去附回饋的輸出排成序列訓練模型）。
- 記憶：用人類記憶類比 —— 感官記憶 ≈ 輸入的 embedding；短期記憶 ≈ 上下文中的學習（受 context window 長度限制）；長期記憶 ≈ 外部向量資料庫，查詢時快速檢索（MIPS，常用 ANN 演算法如 LSH、ANNOY、HNSW、FAISS、ScaNN）。
- 工具使用：MRKL（LLM 當路由器，把問題分派給專家模組）、TALM / Toolformer（微調模型學會呼叫 API）、HuggingGPT（ChatGPT 規劃任務、挑 HuggingFace 模型執行，分四階段）、API-Bank（評測工具使用的三個層次）。
- 案例：ChemCrow（化學領域，13 個專家工具；LLM 自評與人類專家評估結果不一致 → 提醒「讓 LLM 評自己」在專業領域有風險）、Generative Agents（25 個角色的模擬小鎮，記憶流 + 檢索 + 反思 + 規劃）、AutoGPT、GPT-Engineer。
- 作者列出的三大挑戰：
  1. Context 長度有限
  2. 長期規劃與任務拆解困難，遇到意外錯誤時不太會調整計畫
  3. 自然語言介面不可靠（格式錯誤、不聽指令），所以 demo 程式很大比例都在解析模型輸出

## 我的初步判斷

- 適合當 wiki 的「骨架」：三元件框架很好教。
- 年代較早（2023），工具與產品資訊可能過時，但概念框架仍常被引用。
