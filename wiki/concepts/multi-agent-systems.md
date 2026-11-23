---
title: 多 Agent 系統
type: concept
sources: [S3, S4, S5]
updated: 2026-11-23
---

# 多 Agent 系統（Multi-agent systems）

## 先把單一 agent 做到最好

S4 的一般建議是先盡量發揮單一 agent 的能力：多 agent 雖然概念上分工清楚，但會增加複雜度與負擔，很多時候一個 agent 加上工具就夠了 [S4]。

什麼時候考慮拆成多個 agent [S4]：

- **邏輯太複雜**：提示裡有大量 if-then-else 分支，難以維護。
- **工具超載**：問題不只在工具數量，而在工具彼此相似、重疊。有團隊能管好 15 個以上定義清楚的工具，也有團隊不到 10 個重疊的工具就常選錯。

## 兩種多 agent 模式（S4）

| 模式 | 運作方式 | 適合 |
|---|---|---|
| Manager（agent 當工具） | 一個中央 manager agent 透過工具呼叫指揮多個專門 agent，再整合結果 | 只想讓一個 agent 掌控流程並面對使用者 |
| Decentralized（互相交接） | 多個平等的 agent，依專長把工作「handoff」給另一個 agent | 對話分流（例如客服先分類再交給專門 agent） |

（表格整理自 [S4]）

多 agent 系統可以畫成一張「圖」（graph）：agent 是節點；manager 模式的邊是工具呼叫，decentralized 模式的邊是交接 [S4]。

## 與 S3 的關係

S3 的 orchestrator-workers 模式是由中央 LLM 動態拆任務、分派給 worker、再整合結果 [S3]。它和 S4 的 manager 模式結構相似 [整理]。

## 真實案例：Anthropic 的多 agent 研究系統（S5）

- **定義**：多 agent 系統 = 多個 agent（LLM 在迴圈中自主使用工具）一起合作 [S5]。
- **架構**：主研究 agent 分析問題、擬定策略，先把計畫存進記憶（context 超過 200,000 tokens 會被截斷），再平行派出多個子 agent 各自搜尋；子 agent 回報後，主 agent 決定是否需要再研究；最後交給引用 agent 標註每個說法的來源 [S5]。
- **為什麼適合研究**：研究無法事先寫死步驟，需要根據中途發現改變方向；子 agent 各自有獨立的 context，可以平行探索不同面向，再把重點濃縮回報 [S5]。

### 數據

| 項目 | 數字 |
|---|---|
| 多 agent（Opus 4 主 + Sonnet 4 子）vs 單一 Opus 4 | 內部研究評測表現好 90.2% |
| token 用量對表現差異的解釋力（BrowseComp） | 單獨解釋 80% |
| agent 的 token 用量 | 約為一般聊天的 4 倍 |
| 多 agent 系統的 token 用量 | 約為一般聊天的 15 倍 |
| 平行開 3–5 個子 agent + 子 agent 平行用工具 | 複雜問題研究時間最多縮短 90% |

（表格數字皆來自 [S5]）

### 不適合多 agent 的情況

所有 agent 需要共享同一份 context、或彼此高度相依的任務，例如多數寫程式的任務，可平行的部分比研究少，而且 agent 目前還不擅長即時協調與委派 [S5]。

## 觀點差異：單 agent 優先 vs 多 agent 大幅提升？

- S4：一般建議先把單一 agent 做到極致，多 agent 會增加複雜度 [S4]。
- S5：在研究任務上，多 agent 比單 agent 好 90.2% [S5]。
- 整合：兩者不矛盾，而是**適用條件不同**。S5 自己也指出，多 agent 只適合可大量平行、資訊量超過單一 context、價值高到值得付出約 15 倍 token 成本的任務 [S5]。

## 相關頁面

- [Workflow 模式](workflow-patterns.md)
- [Agent 迴圈](agent-loop.md)
- [評估](evaluation.md)
- [何時該用 Agent](when-to-use-agents.md)

## 來源

- [S3](../sources/s3-anthropic-bea.md)
- [S4](../sources/s4-openai-guide.md)
- [S5](../sources/s5-anthropic-multi-agent.md)
