---
title: AI Agent 的定義
type: concept
sources: [S1, S3, S4]
updated: 2026-11-23
---

# AI Agent 的定義

## S1 的定義：LLM 大腦 + 三元件

在 LLM 驅動的自主 agent 系統中，LLM 扮演「大腦」，再搭配三個關鍵元件 [S1]：

1. **規劃（Planning）**：拆解任務、自我反思 [S1] → 見 [規劃](planning.md)
2. **記憶（Memory）**：短期與長期記憶 [S1] → 見 [記憶](memory.md)
3. **工具使用（Tool use）**：呼叫外部 API 取得模型權重裡沒有的資訊或能力 [S1] → 見 [工具使用](tool-use.md)

## S3 的定義：看「誰決定流程」

S3 指出「agent」這個詞被用在很多不同的系統上，所以先把全部統稱為 agentic systems，再區分 [S3]：

- **Workflow**：LLM 和工具按照預先寫好的程式路徑被編排。
- **Agent**：LLM 自己動態決定流程與工具使用，掌控完成任務的方式。

詳見 [Workflows vs Agents](workflows-vs-agents.md)。

## S4 的定義：代替你完成任務的系統

Agent 是能代替使用者、相當獨立地完成任務的系統 [S4]。它有兩個核心特徵 [S4]：

1. 用 LLM 管理工作流程的執行與決策：知道什麼時候完成、會主動修正，失敗時能停下來把控制權交還給使用者。
2. 能使用工具和外部系統互動（拿資訊、採取行動），依當下狀態挑選工具，並在清楚的防護欄內運作。

**不算 agent 的例子**：簡單聊天機器人、單輪 LLM、情緒分類器——它們有用到 LLM，但 LLM 沒有控制工作流程的執行 [S4]。

## 兩種「三元件」別搞混

| S1：agent 的能力 | S4：打造 agent 需要的零件 |
|---|---|
| 規劃 | 模型（負責推理與決策） |
| 記憶 | 工具（外部函式或 API） |
| 工具使用 | 指令（行為準則與防護欄） |

（左欄依 [S1]，右欄依 [S4]；並列對照為 [整理]）

## 觀點差異

- S1 偏「元件觀點」：有 LLM 大腦 + 規劃 / 記憶 / 工具，就是 agent 系統 [S1]。
- S3 偏「控制權觀點」：即使有工具和記憶，只要流程是程式寫死的，就叫 workflow [S3]。
- S4 也偏「控制權觀點」：關鍵是 LLM 有沒有控制工作流程的執行 [S4]。
- **共同點**：三者都要求 LLM 不只是聊天，而是會使用工具、與外部世界互動 [整理]。

## 本 wiki 採用的教學定義

> **AI Agent = 會自己決定下一步、會使用工具、在迴圈中把任務完成的 AI 系統。** [整理，綜合 S1、S3、S4]

可以用「控制權光譜」幫助理解 [整理]：

```
聊天機器人 ──────── Workflow ──────── Agent
 (只回答)        (會用工具，         (會用工具，
                 但步驟寫死)          自己決定步驟)
```

## 相關頁面

- [Workflows vs Agents](workflows-vs-agents.md)
- [Agent 迴圈](agent-loop.md)
- [Augmented LLM](augmented-llm.md)
- [挑戰與風險](challenges-and-risks.md)

## 來源

- [S1](../sources/s1-weng-2023.md)
- [S3](../sources/s3-anthropic-bea.md)
- [S4](../sources/s4-openai-guide.md)
