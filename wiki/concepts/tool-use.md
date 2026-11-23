---
title: 工具使用（Tool use）
type: concept
sources: [S1, S3, S4, S5]
updated: 2026-11-23
---

# 工具使用（Tool use）

## 為什麼 agent 需要工具？

模型權重在預訓練後很難改變，所以 agent 要透過呼叫外部 API 取得權重裡沒有的東西：最新資訊、執行程式碼的能力、私有資料來源等 [S1]。

## 代表性做法

- **MRKL**：一組「專家模組」（可以是神經網路，也可以是計算機、匯率轉換、天氣 API），LLM 當路由器把問題分派給最合適的模組 [S1]。實驗發現 LLM 不一定能正確抽出計算所需的參數 → 「知道何時用、怎麼用工具」才是關鍵 [S1]。
- **TALM / Toolformer**：微調語言模型，讓它學會呼叫外部工具 API [S1]。
- **ChatGPT Plugins、Function calling**：實務上讓 LLM 使用工具的例子 [S1]。
- **HuggingGPT**：ChatGPT 當任務規劃者，分四階段：任務規劃 → 選模型 → 執行 → 產生回應 [S1]。
- **API-Bank**：評測工具使用能力的基準，分三層：會不會呼叫 API、會不會找到對的 API、能不能規劃多次 API 呼叫 [S1]。

## 工具的三種類型

S4 把 agent 需要的工具分成三類 [S4]：

| 類型 | 用途 | 例子 |
|---|---|---|
| 資料（Data） | 取得執行任務需要的資訊 | 查資料庫、讀 PDF、搜尋網路 |
| 行動（Action） | 對外部系統採取動作 | 寄信、更新客戶紀錄、把工單轉給真人 |
| 編排（Orchestration） | 其他 agent 本身也可以當成工具 | 退款 agent、研究 agent、寫作 agent |

S4 也建議每個工具都要有標準化定義、文件清楚、經過測試、可重複使用；需要的工具越來越多時，可以考慮拆成多個 agent [S4]。

## ACI：給 agent 用的介面也要好好設計

S3 主張：人們花多少心力設計人機介面（HCI），就該花多少心力設計 **agent-computer interface（ACI）**；工具的定義與說明要和整體提示一樣認真做提示工程 [S3]。

具體建議 [S3]：

- 站在模型的角度：光看說明和參數，能不能一眼看懂怎麼用？好的工具說明包含使用範例、邊界情況、輸入格式、和其他工具的差別。
- 把參數名稱和說明寫得像給新進工程師看的好文件。
- 實際測試模型怎麼用工具，看它犯哪些錯，再改。
- **防呆（poka-yoke）**：改變參數設計，讓模型更難犯錯。
- 格式盡量接近模型在網路上常見的文字格式，避免需要大量跳脫字元或精確計數的格式。

**案例**：Anthropic 打造 SWE-bench 程式 agent 時，花在優化工具的時間比優化整體提示還多；模型在離開根目錄後常把相對路徑弄錯，改成強制使用絕對路徑後，模型就用得完全正確 [S3]。

**案例 2**：S5 做了一個「測試工具的 agent」，讓它反覆使用有問題的工具並改寫工具說明；之後的 agent 用新說明，完成任務的時間減少 40% [S5]。S5 也指出，工具說明寫得差，可能讓 agent 從一開始就走錯方向 [S5]。

## 相關頁面

- [AI Agent 的定義](ai-agent-definition.md)
- [規劃](planning.md)
- [Augmented LLM](augmented-llm.md)
- [Agent 迴圈](agent-loop.md)

## 來源

- [S1](../sources/s1-weng-2023.md)
- [S3](../sources/s3-anthropic-bea.md)
- [S4](../sources/s4-openai-guide.md)
- [S5](../sources/s5-anthropic-multi-agent.md)
