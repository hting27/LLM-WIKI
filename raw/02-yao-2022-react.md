# S2 — ReAct: Synergizing Reasoning and Acting in Language Models

- 作者：Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao（Princeton / Google Research）
- 日期：arXiv 2022-10-06 首次提交；ICLR 2023 發表
- 網址：https://arxiv.org/abs/2210.03629
- 類型：學術論文
- 取得方式：摘要、引言、Google Research 部落格說明（2026-11-23）
- 版權說明：本檔只存放閱讀筆記（自行改寫）。

## 閱讀筆記（改寫）

- 問題：過去「推理」（例如 chain-of-thought）和「行動」（例如產生行動計畫）是分開研究的。
- 方法：讓 LLM **交錯**產生「推理軌跡」與「任務行動」。
  - 推理幫助模型擬定、追蹤、更新計畫，以及處理例外（reason to act）。
  - 行動讓模型能去外部（知識庫、環境）拿到新資訊，再拿來推理（act to reason）。
- 格式大致是：Thought → Action → Observation，重複多次。
- 結果：
  - 問答（HotpotQA）與事實查核（FEVER）：透過一個簡單的 Wikipedia API 取得資訊，減少只靠 chain-of-thought 時常見的幻覺與錯誤傳遞問題。
  - 互動決策任務（ALFWorld、WebShop）：只用 1–2 個範例提示，成功率分別比模仿學習與強化學習方法**絕對提升 34% 與 10%**。
  - 推理軌跡讓人比較看得懂模型在做什麼 → 可解釋、可信、可除錯。
- 也嘗試用 ReAct 格式的成功軌跡去微調較小的模型。

## 我的初步判斷

- 這是「agent 迴圈」最經典的原始出處，教學上可以用來說明「想 → 做 → 看結果」。
- 注意：S1 把 ReAct 放在「自我反思」底下介紹，但論文本身的定位是「推理 + 行動的結合」。
