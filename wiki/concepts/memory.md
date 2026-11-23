---
title: 記憶（Memory）
type: concept
sources: [S1, S5]
updated: 2026-11-23
---

# 記憶（Memory）

## 用人類記憶來類比

S1 用人類記憶的分類，粗略對應到 LLM agent [S1]：

| 人類記憶 | 特性 | 對應到 agent |
|---|---|---|
| 感官記憶 | 只維持幾秒 | 把原始輸入（文字、圖片）轉成向量表示（embedding） |
| 短期 / 工作記憶 | 容量小、時間短 | 上下文中的學習（in-context learning），受 context window 長度限制 |
| 長期記憶 | 容量幾乎無限、可保存很久 | 外部向量資料庫，需要時快速檢索 |

（表格內容整理自 [S1]）

## 長期記憶怎麼查？

常見做法是把資訊的向量存進向量資料庫，用「最大內積搜尋（MIPS）」找最相近的資料；為了速度，通常用近似最近鄰（ANN）演算法，犧牲一點準確度換取大幅加速，例如 LSH、ANNOY、HNSW、FAISS、ScaNN [S1]。

> 教學註記：對初學者只需要知道「長期記憶 ≈ 可以查詢的外部資料庫」，演算法細節不必講 [整理]。

## 實務：把重要的東西寫到外部

- S5 的研究系統中，主 agent 一開始就把研究計畫存到記憶，因為 context 超過 200,000 tokens 會被截斷，計畫不能跟著消失 [S5]。
- 長時間對話中，agent 會先摘要已完成的階段、把重點存到外部記憶，再繼續下一個任務 [S5]。
- 子 agent 直接把成果寫進檔案系統、只回傳一個參照，避免層層轉述造成的「傳話遊戲」失真 [S5]。

## 相關頁面

- [AI Agent 的定義](ai-agent-definition.md)
- [挑戰與風險](challenges-and-risks.md)：context 長度有限

## 來源

- [S1](../sources/s1-weng-2023.md)
- [S5](../sources/s5-anthropic-multi-agent.md)
