---
title: Workflows vs Agents
type: concept
sources: [S3, S4]
updated: 2026-11-23
---

# Workflows vs Agents

## 兩種 agentic system

S3 把所有「LLM + 工具」的系統統稱為 **agentic systems**，再依「誰決定流程」分成兩種 [S3]：

| | Workflow（工作流） | Agent（代理） |
|---|---|---|
| 流程由誰決定 | 工程師預先寫好的程式路徑 | LLM 自己動態決定 |
| 適合 | 定義清楚、可拆成固定步驟的任務 | 開放式問題，無法預測需要幾步 |
| 優點 | 可預測、一致 | 有彈性、能處理意外 |
| 代價 | 遇到沒預料到的情況就卡住 | 成本較高、錯誤可能累積 |

（表格整理自 [S3]）

## S4 的對照

S4 沒有用「workflow vs agent」這組詞，而是把 workflow 當成「要完成使用者目標所需的一連串步驟」，再看是不是由 LLM 控制這些步驟的執行；沒有讓 LLM 控制流程的應用（如單輪 LLM、分類器）就不算 agent [S4]。兩者的判準本質上相同：**LLM 有沒有掌控流程** [整理]。

## 一個生活化的比喻

- Workflow 像照著食譜做菜：步驟固定，每一步做什麼都寫好了 [整理]。
- Agent 像請一位廚師「用冰箱裡有的東西做晚餐」：他要自己看有什麼、決定做什麼、試味道再調整 [整理]。

## 相關頁面

- [AI Agent 的定義](ai-agent-definition.md)
- [Workflow 模式](workflow-patterns.md)
- [何時該用 Agent](when-to-use-agents.md)

## 來源

- [S3](../sources/s3-anthropic-bea.md)
- [S4](../sources/s4-openai-guide.md)
