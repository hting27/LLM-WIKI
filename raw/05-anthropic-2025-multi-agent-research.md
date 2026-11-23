# S5 — How we built our multi-agent research system

- 作者：Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford（Anthropic Engineering）
- 日期：2025-06-13
- 網址：https://www.anthropic.com/engineering/multi-agent-research-system
- 類型：業界工程案例
- 取得方式：網頁全文閱讀（2026-11-23）
- 版權說明：本檔只存放閱讀筆記（自行改寫）。

## 閱讀筆記（改寫）

- 定義：multi-agent 系統 = 多個 agent（LLM 在迴圈中自主使用工具）一起合作。
- 為何研究適合 agent：研究問題無法事先寫死步驟，要根據中途發現改變方向；一次性的線性流程做不到。
- 架構：**orchestrator-worker**。主研究 agent（Lead Researcher）分析問題、擬策略、把計畫存到記憶（context 超過 200,000 tokens 會被截斷，所以計畫要另外保存），再平行派出子 agent 各自搜尋；最後交給 CitationAgent 標註引用來源。
- 數據：
  - Claude Opus 4 當主 agent + Claude Sonnet 4 子 agent，在內部研究評測上比單一 Claude Opus 4 **好 90.2%**。
  - 在 BrowseComp 評測中，**token 用量單獨就解釋 80% 的表現差異**（加上工具呼叫次數與模型選擇共解釋 95%）。
  - 成本：agent 約用聊天的 **4 倍** token，多 agent 系統約 **15 倍**。
  - 主 agent 一次平行開 3–5 個子 agent、子 agent 平行用 3 個以上工具 → 複雜問題研究時間最多縮短 **90%**。
  - 讓 agent 自己測試並改寫有問題的工具說明 → 後續 agent 完成任務時間減少 **40%**。
- 不適合 multi-agent 的情況：所有 agent 需要共享同一份 context、或彼此高度相依（例如多數寫程式任務）。
- 八條提示工程原則（改寫）：站在 agent 角度模擬觀察；教主 agent 怎麼委派（目標、輸出格式、工具、邊界）；依問題難度決定投入多少；工具設計與選擇很關鍵；讓 agent 改進自己；先廣後窄的搜尋策略；引導思考過程；平行呼叫工具。
- 早期失敗：簡單問題開 50 個子 agent、無止盡地找不存在的資料、子 agent 互相重複工作。
- 評估：
  - **立刻用小樣本開始評估**（約 20 個真實問題就能看出大幅變化）。
  - **LLM-as-judge**：一個評審提示依量表打分 —— 事實正確、引用正確、完整性、來源品質、工具效率。
  - **人工評估**抓自動化漏掉的問題：例如早期 agent 偏好 SEO 內容農場而非學術 PDF。
- 正式上線的挑戰：agent 有狀態、錯誤會累積 → 需要能從中斷處繼續；非確定性讓除錯困難 → 需要完整追蹤；部署要用漸進式（rainbow deployment）；同步執行造成瓶頸。
- 附錄重點：會改變狀態的 agent 用「最終狀態」評估；長對話要摘要後存到外部記憶；子 agent 直接把成果寫入檔案系統，避免「傳話遊戲」造成資訊失真。

## 我的初步判斷

- 提供了 S4「先單 agent」建議的另一面：在研究這種可平行的任務上，多 agent 有明確好處，但代價是 token。
- 「評估」這一主題在前四篇都很少，這篇補上了。
