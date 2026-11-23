# Wiki 操作紀錄（append-only）

## [2026-11-23] ingest | S1 Weng (2023)

- 討論：discussions/ingest-01.md
- 新增：sources/s1-weng-2023.md、concepts/ai-agent-definition.md、planning.md、memory.md、tool-use.md、challenges-and-risks.md
- 刻意不收錄：MIPS 演算法細節、Chain of Hindsight 訓練細節（對初學者太深）

## [2026-11-23] lint | 第 1 輪

- 結果：0 錯誤、3 警告（見 lint-history/round-01.txt）
- 修正：ai-agent-definition 清單補 [S1]；所有概念頁加「## 來源」區塊，解決 sources 頁孤立問題（並寫入 AGENTS.md 規則）
- 發現 lint 本身誤判：純連結清單被當成「沒來源的段落」→ 修正 lint_wiki.py

## [2026-11-23] ingest | S2 ReAct

- 討論：discussions/ingest-02.md
- 新增：sources/s2-react.md、concepts/react.md、concepts/agent-loop.md
- 修改：planning.md（加「觀點差異」：ReAct 分類）、challenges-and-risks.md（只推理不行動的問題）
- lint 第 2 輪：3 錯誤（index 未更新）、2 警告（修改了頁面內文卻忘了更新 frontmatter sources）→ 已修正

## [2026-11-23] ingest | S3 Anthropic Building effective agents

- 討論：discussions/ingest-03.md
- 新增：sources/s3-anthropic-bea.md、concepts/workflows-vs-agents.md、augmented-llm.md、workflow-patterns.md、when-to-use-agents.md
- 修改：ai-agent-definition.md（加 S3 定義與「觀點差異」）、agent-loop.md（四要素）、tool-use.md（ACI）、challenges-and-risks.md（成本與錯誤累積）
- 本輪開始在生成當下就同步 frontmatter / 來源區塊 / index（AGENTS.md §4 新增檢查清單）

## [2026-11-23] ingest | S4 OpenAI practical guide

- 討論：discussions/ingest-04.md
- 新增：sources/s4-openai-guide.md、concepts/guardrails-human-oversight.md、concepts/multi-agent-systems.md、glossary.md
- 修改：ai-agent-definition.md（S4 定義、兩種三元件對照、教學定義、控制權光譜）、agent-loop.md（結束條件）、tool-use.md（工具三類）、when-to-use-agents.md（三條件）、workflows-vs-agents.md（S4 對照）
- 新工具：scripts/add_source.py，自動同步 frontmatter / 來源區塊 / index

## [2026-11-23] ingest | S5 Anthropic multi-agent research system

- 討論：discussions/ingest-05.md
- 新增：sources/s5-anthropic-multi-agent.md、concepts/evaluation.md
- 修改：multi-agent-systems.md（案例、數據、「觀點差異」：單 vs 多 agent）、workflow-patterns.md、memory.md、tool-use.md、challenges-and-risks.md、when-to-use-agents.md
- 自我檢查時發現：multi-agent-systems.md 把「S3 orchestrator ≈ S4 manager」這個自己的比較標成 [S3] → 改標 [整理]（lint 抓不到這種錯，只能靠人讀）

## [2026-11-23] query | 產生簡報

- 大綱：slides/outline.md（17 頁，每頁對應 wiki 頁面）
- check_slides 第 1 次：2 個問題——簡報自行編造範例數字「降雨機率 70%」（wiki 沒有）、封面的「LLM」未解釋 → 範例改寫進 concepts/react.md（標 [整理]、不放數字）再引用；AGENTS.md §7 新增第 6 條
- check_slides 第 2 次：全部通過
- 視覺檢查（截圖）：封面 SVG 標籤被裁切、ReAct 頁標籤與文字重疊 → 修正；新增 scripts/visual_check.py 成為固定步驟
