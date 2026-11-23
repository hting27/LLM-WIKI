---
title: ReAct（推理 + 行動）
type: concept
sources: [S1, S2]
updated: 2026-11-23
---

# ReAct（Reason + Act）

## 核心想法

以前「推理」（例如 chain-of-thought）和「行動」（例如產生行動計畫）是分開研究的；ReAct 讓 LLM **交錯**進行兩者 [S2]：

- **推理 → 行動**：推理幫模型擬定、追蹤、更新計畫，並處理例外狀況 [S2]。
- **行動 → 推理**：行動讓模型能從外部（知識庫、環境）拿到新資訊，再拿來推理 [S2]。

## 格式

```
Thought:     我需要先知道 X
Action:      search("X")
Observation: 搜尋結果……
Thought:     根據結果，接下來應該……
...（重複直到完成）
```

（格式依 [S1] 對 ReAct 的說明整理）

## 教學範例（給初學者）

以下是為了教學自行設計的情境，不是來源中的實驗；刻意不放任何數字，以免被誤認為真實資料 [整理]：

```
任務：明天出門要不要帶傘？
Thought:     我需要知道明天的天氣。
Action:      search_weather("台北", "明天")
Observation: 天氣服務回傳：明天下午有雨。
Thought:     會下雨，建議帶傘。→ 給出答案
```

## 為什麼有效？

- 只推理不行動：模型只能靠記憶，容易產生幻覺，而且一步錯會一路錯 [S2]。
- ReAct 透過工具（例如 Wikipedia API）查證，降低這些問題 [S2]。
- 在 ALFWorld 與 WebShop 兩個互動任務中，成功率分別絕對提升 34% 與 10% [S2]。
- 推理過程寫出來，人可以看懂、可以除錯 [S2]。

## 觀點差異

- S1 把 ReAct 放在「自我反思」底下介紹 [S1]。
- S2 原論文把 ReAct 定位成「推理與行動的結合」這個通用範式 [S2]。
- 本 wiki 的處理：ReAct 視為 [Agent 迴圈](agent-loop.md) 的代表性實作，同時保留它在 [規劃](planning.md) 頁的位置 [整理]。

## 相關頁面

- [Agent 迴圈](agent-loop.md)
- [規劃](planning.md)
- [工具使用](tool-use.md)

## 來源

- [S1](../sources/s1-weng-2023.md)
- [S2](../sources/s2-react.md)
