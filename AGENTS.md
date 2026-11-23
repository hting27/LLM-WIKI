# AGENTS.md — 本 Wiki 的規則檔（Schema）

> 這份檔案是給 LLM 看的「工作規則」。每次 ingest、查詢、產生簡報之前，LLM 都必須先讀這份檔案。
> 概念來自 Karpathy 的 LLM Wiki：人負責挑資料、提問、做決定；LLM 負責摘要、交叉連結、歸檔與維護。

## 1. 主題與讀者

- 主題：**AI Agents（AI 代理）**
- 最終用途：製作「AI Agents 是什麼？」教學 HTML 簡報
- 目標讀者：沒有 AI 背景、但會用 ChatGPT 之類聊天機器人的大學生

## 2. 目錄結構

```
raw/            原始資料的閱讀筆記與來源資訊（只新增、不修改）
discussions/    每次 ingest 前的「先討論」紀錄（人確認後才可寫入 wiki/）
wiki/
  index.md      所有頁面目錄 + 一句話摘要（每次 ingest 都要更新）
  log.md        時間序操作紀錄（append-only）
  lint-report.md 最近一次檢查結果
  sources/      每篇來源一頁摘要（s1-xxx.md …）
  concepts/     概念頁（一個概念一頁）
slides/         由 wiki 產生的簡報、大綱、事實檢查表
scripts/        自動檢查工具（lint_wiki.py、check_slides.py）
```

## 3. 來源代碼

| 代碼 | 來源 |
|---|---|
| S1 | Lilian Weng (2023). *LLM Powered Autonomous Agents* |
| S2 | Yao et al. (2022/ICLR 2023). *ReAct: Synergizing Reasoning and Acting in Language Models* |
| S3 | Anthropic (2024). *Building effective agents* |
| S4 | OpenAI (2025). *A practical guide to building agents* |
| S5 | Anthropic (2025). *How we built our multi-agent research system* |

新增來源時代碼依序遞增（S6, S7…），並同步更新本表與 `wiki/index.md`。

## 4. Ingest 流程（先討論、後生成）

1. **讀取**：閱讀原文，在 `raw/NN-名稱.md` 記下書目資訊與「用自己的話」整理的筆記（不貼原文長段落）。
2. **討論**：在 `discussions/ingest-NN.md` 寫下：
   - 這篇的 3–5 個核心主張
   - 和既有 wiki 頁面「重疊 / 補充 / 衝突」的地方
   - 提議：要新增哪些頁、修改哪些頁
   - 待人決定的問題
3. **人確認**：人在討論紀錄最後寫「決定」，沒有決定前**不得**寫入 `wiki/`。
4. **生成**：寫 `wiki/sources/sN-*.md`，再新增或更新 `wiki/concepts/` 中的頁面。
   **每改一頁就同步完成**（第 2 輪 lint 後加入，把檢查從 lint 提前到生成當下）：
   - [ ] frontmatter `sources` 加上新來源代碼
   - [ ] `## 來源` 區塊加上新來源頁連結
   - [ ] `index.md` 該列的來源欄位同步
5. **登錄**：更新 `wiki/index.md`、在 `wiki/log.md` 追加一筆紀錄。
6. **檢查**：執行 `python3 scripts/lint_wiki.py`，有錯誤就修到通過才算完成這一輪。

## 5. 頁面格式

每個 wiki 頁面開頭必須有 frontmatter：

```
---
title: 頁面標題
type: concept | source | meta
sources: [S1, S3]
updated: YYYY-MM-DD
---
```

- 每一個**事實性主張**後面都要標來源代碼，例如 `…會迭代修正 [S3]`。
- 教學用的比喻或作者自己的整理，標 `[整理]`，不可偽裝成來源內容。
- 檔名：小寫英文 + 連字號，例如 `agent-loop.md`。
- 頁面之間用相對路徑 Markdown 連結互相引用。
- 每個概念頁最後要有 `## 來源` 區塊，連結到對應的 `sources/` 頁面（第 1 輪 lint 發現來源頁變成孤立頁面後加入此規則）。

## 6. 衝突處理

不同來源說法不同時，**不要覆蓋**舊內容，改在頁面中加一個 `## 觀點差異` 區塊，分別寫出各來源的說法與脈絡。

## 7. 產生簡報的規則

1. 只能使用 `wiki/` 裡的內容，不可加入 wiki 沒有的事實或數字。
2. 先產生 `slides/outline.md`（每頁：要講的一個概念 + 依據的 wiki 頁面），人確認後才產生 HTML。
3. HTML 每一張投影片的 `<section>` 必須有 `data-wiki="concepts/xxx.md,…"` 屬性。
4. 產生後執行 `python3 scripts/check_slides.py`，數字與引用必須全部能在 wiki 中找到。
5. 每頁只講一個概念；第一次出現的英文術語要附中文解釋。
6. **教學範例也要先寫進 wiki**（標 `[整理]`）再拿到簡報用；範例中不放假數字。（第 1 次 check_slides 抓到簡報自行編了「降雨機率 70%」後加入）

## 8. Lint 規則（`scripts/lint_wiki.py` 會自動檢查）

- 失效連結（連到不存在的頁面）
- 孤立頁面（沒有任何頁面連到它，index 除外）
- 缺少 frontmatter 或缺少 `sources` 欄位
- 使用了未登錄的來源代碼
- `index.md` 沒有列出的頁面
- 概念頁中完全沒有來源標註的段落過多
