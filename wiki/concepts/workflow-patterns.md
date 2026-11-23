---
title: 五種 Workflow 模式
type: concept
sources: [S3, S5]
updated: 2026-11-23
---

# 五種常見的 Workflow 模式

S3 整理出正式產品中常見、可以自由組合的五種模式 [S3]：

| 模式 | 怎麼運作 | 什麼時候用 | 例子 |
|---|---|---|---|
| Prompt chaining（提示鏈） | 拆成固定步驟，上一步輸出是下一步輸入；中間可加程式檢查（gate） | 任務能乾淨拆成固定子任務 | 先寫大綱 → 檢查大綱 → 再寫全文 |
| Routing（路由） | 先分類輸入，再送到專門的處理流程 | 有明確類別、分類可以做得準 | 客服問題分流：一般問題 / 退款 / 技術支援 |
| Parallelization（平行化） | Sectioning：拆成獨立子任務同時做；Voting：同一任務做多次 | 想加速，或需要多個觀點提高信心 | 多個提示同時審查程式碼漏洞 |
| Orchestrator-workers（指揮者-工人） | 中央 LLM 動態拆任務、分派、整合 | 無法事先知道需要哪些子任務 | 需要修改多個檔案的程式任務 |
| Evaluator-optimizer（評估者-優化者） | 一個產生、一個評估回饋，迴圈改進 | 有清楚評估標準、迭代確實有幫助 | 文學翻譯：評估者指出譯者漏掉的細節 |

（表格整理自 [S3]）

## 重點

- 這些模式不是規定，而是可以組合、客製的積木；只在能證明效果更好時才增加複雜度 [S3]。
- Orchestrator-workers 和平行化看起來很像，差別在子任務是「事先定好」還是「由指揮者依輸入決定」 [S3]。
- 真實案例：Anthropic 的研究功能就是用 orchestrator-worker 架構，主 agent 協調、子 agent 平行搜尋 [S5]。詳見 [多 Agent 系統](multi-agent-systems.md)。

## 相關頁面

- [Workflows vs Agents](workflows-vs-agents.md)
- [Augmented LLM](augmented-llm.md)

## 來源

- [S3](../sources/s3-anthropic-bea.md)
- [S5](../sources/s5-anthropic-multi-agent.md)
