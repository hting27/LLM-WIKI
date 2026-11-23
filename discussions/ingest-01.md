# Ingest 01 討論紀錄 — S1 Weng (2023)

日期：2026-11-23　｜　Wiki 狀態：空白（第一篇）

## 1. 這篇的核心主張

1. Agent = LLM 當大腦 + 規劃 + 記憶 + 工具使用。
2. 規劃包含「任務拆解」與「自我反思」兩件事。
3. 記憶可以用人類記憶分類來對應：短期記憶 ≈ context，長期記憶 ≈ 外部向量庫。
4. 目前三大挑戰：context 有限、長期規劃困難、自然語言介面不可靠。

## 2. 與既有 Wiki 的關係

- 第一篇，沒有重疊或衝突。
- 這篇會決定 wiki 的初始骨架，所以要注意：之後的來源可能會挑戰這個框架，概念頁要寫得容易擴充。

## 3. 提議的頁面變更

| 動作 | 頁面 | 理由 |
|---|---|---|
| 新增 | sources/s1-weng-2023.md | 來源摘要 |
| 新增 | concepts/ai-agent-definition.md | 先放 S1 的定義，之後再補其他來源 |
| 新增 | concepts/planning.md | 任務拆解 + 自我反思 |
| 新增 | concepts/memory.md | 記憶類比 |
| 新增 | concepts/tool-use.md | MRKL、Toolformer、HuggingGPT |
| 新增 | concepts/challenges-and-risks.md | 三大挑戰 |
| 暫不新增 | MIPS / ANN 演算法細節 | 對初學者太深，只在 memory 頁提一句 |
| 暫不新增 | Chain of Hindsight、Algorithm Distillation | 屬於訓練方法，不是初學者必要知識 |

## 4. 待決定的問題

- Q1：ReAct 要不要獨立成頁？S1 只是把它放在自我反思底下。
- Q2：案例（ChemCrow、Generative Agents）要放哪？

## 5. 決定

- Q1：先不獨立，等 S2（ReAct 原始論文）ingest 時再決定。
- Q2：放在 sources 頁即可；ChemCrow「LLM 自評不可靠」的發現放進 challenges-and-risks。
- 同意第 3 節的頁面變更。

