# Ingest 02 討論紀錄 — S2 ReAct (Yao et al.)

日期：2026-11-23　｜　Wiki 狀態：1 個來源、5 個概念頁

## 1. 這篇的核心主張

1. 推理（reasoning）和行動（acting）以前被分開研究，應該交錯進行。
2. 格式：Thought → Action → Observation，反覆循環。
3. 推理幫忙決定下一步行動；行動帶回新資訊幫助推理。
4. 實驗：問答與事實查核任務中減少幻覺；ALFWorld / WebShop 成功率分別絕對提升 34% 與 10%。
5. 推理軌跡讓人看得懂、可以除錯。

## 2. 與既有 Wiki 的關係

- **重疊**：planning.md 已依 S1 提到 ReAct（放在「自我反思」底下）。
- **衝突（分類上的）**：S1 把 ReAct 歸類為自我反思；但 S2 原論文的定位是「推理 + 行動的結合」，它其實是 agent 運作迴圈本身，不只是反思技巧。
- **補充**：S1 沒有提到具體數據；S2 提供可引用的實驗結果。

## 3. 提議的頁面變更

| 動作 | 頁面 | 理由 |
|---|---|---|
| 新增 | sources/s2-react.md | 來源摘要 |
| 新增 | concepts/react.md | 回答 Q1：值得獨立成頁，它是後面「agent 迴圈」的原型 |
| 新增 | concepts/agent-loop.md | 「想→做→看」的通用迴圈概念頁，ReAct 是其中一種實作 |
| 修改 | concepts/planning.md | 在 ReAct 處加 `## 觀點差異`，說明分類差異並連到 react.md |
| 修改 | concepts/challenges-and-risks.md | 補「只推理不行動 → 幻覺與錯誤傳遞」 |

## 4. 待決定的問題

- Q3：agent-loop 是 S2 才有的概念嗎？S1 沒有明講「迴圈」。

## 5. 決定

- Q3：先以 S2 為來源建立 agent-loop.md，之後若其他來源有更一般的說法再補上。
- 同意第 3 節變更；planning.md 不刪除原本 S1 的分類，只加觀點差異區塊（依 AGENTS.md §6）。
