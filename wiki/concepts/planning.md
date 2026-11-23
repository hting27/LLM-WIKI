---
title: 規劃（Planning）
type: concept
sources: [S1, S2]
updated: 2026-11-23
---

# 規劃（Planning）

複雜任務通常有很多步驟，agent 需要知道有哪些步驟並事先規劃 [S1]。規劃包含兩件事：任務拆解與自我反思 [S1]。

## 任務拆解（Task decomposition）

- **Chain of Thought（CoT，思維鏈）**：要求模型「一步一步想」，把難題拆成小步驟，也讓人看得到模型的思考過程 [S1]。
- **Tree of Thoughts（思維樹）**：每一步產生多個可能的想法，形成樹狀結構，再用廣度或深度優先搜尋探索 [S1]。
- 拆解的方法可以是：簡單提示（例如「XYZ 的步驟有哪些？」）、任務專屬指令（例如寫小說前先「寫大綱」）、或由人提供 [S1]。
- **LLM+P**：把長期規劃外包給傳統的規劃器，LLM 只負責把問題翻譯成規劃語言（PDDL）再翻譯回來；但前提是該領域已有現成的規劃描述，在機器人領域較常見 [S1]。

## 自我反思（Self-reflection）

讓 agent 檢討過去的行動、修正錯誤，在必須反覆試錯的真實任務中特別重要 [S1]。

- **ReAct**：讓模型交錯產生「推理」與「行動」 [S1]。詳見 [ReAct](react.md)。
- **Reflexion**：失敗後產生一段反思文字，放進工作記憶（最多三則）供下次參考；也會偵測無效率或幻覺的軌跡並重新開始 [S1]。
- **Chain of Hindsight**：把過去附有回饋的多次輸出排成序列，訓練模型學會逐步改進 [S1]。

## 觀點差異

- S1 把 ReAct 歸類在「自我反思」 [S1]；S2 原論文則把它定位為推理與行動交錯的通用範式，而不只是反思技巧 [S2]。
- 兩種分類都保留：在本頁它是自我反思的一種方法；在 [Agent 迴圈](agent-loop.md) 頁它是迴圈的原型 [整理]。

## 相關頁面

- [AI Agent 的定義](ai-agent-definition.md)
- [記憶](memory.md)
- [ReAct](react.md)

## 來源

- [S1](../sources/s1-weng-2023.md)
- [S2](../sources/s2-react.md)
