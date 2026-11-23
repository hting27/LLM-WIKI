---
title: Agent 迴圈（思考 → 行動 → 觀察）
type: concept
sources: [S2, S3, S4]
updated: 2026-11-23
---

# Agent 迴圈

## 基本形狀

Agent 不是「問一次、答一次」，而是反覆執行一個迴圈：先推理要做什麼、採取行動、觀察環境回傳的結果，再根據結果決定下一步 [S2]。S3 也用幾乎相同的方式描述 agent：通常只是「LLM 在迴圈中，根據環境回饋使用工具」 [S3]。

```
   ┌─────────── 思考（Thought）───────────┐
   │                                      ▼
 觀察（Observation）  ◀────────  行動（Action）
```

## 迴圈的四個要素

1. **起點**：agent 從人的指令或與人的討論開始；任務清楚後，自己規劃並執行 [S3]。
2. **每一步都要拿到「真實回饋」**：例如工具呼叫的結果、程式執行結果，用來判斷進度 [S3]。
3. **人類檢查點**：可以在檢查點或遇到阻礙時暫停，等人回饋 [S3]。
4. **停止條件**：任務完成就結束，也常設最大迭代次數之類的停止條件，以保持控制 [S3]。

## 常見的結束條件

S4 指出每個 agent 都需要一個「run」——通常就是一個 while 迴圈，持續執行直到達成結束條件 [S4]：

- 呼叫了代表「最終輸出」的工具
- 模型回覆時不再呼叫任何工具（例如直接回答使用者）
- 發生錯誤
- 達到最大輪數

## 和一般聊天的差別

一般聊天是一問一答；agent 迴圈中，模型可以在給出最終答案前，多次使用工具、取得新資訊並修正計畫 [S2]。

## 代表性實作

- [ReAct](react.md)：Thought → Action → Observation [S2]

## 相關頁面

- [ReAct](react.md)
- [工具使用](tool-use.md)
- [AI Agent 的定義](ai-agent-definition.md)
- [Workflows vs Agents](workflows-vs-agents.md)

## 來源

- [S2](../sources/s2-react.md)
- [S3](../sources/s3-anthropic-bea.md)
- [S4](../sources/s4-openai-guide.md)
