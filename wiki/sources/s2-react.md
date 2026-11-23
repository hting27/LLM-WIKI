---
title: "S2 — ReAct (Yao et al., 2022/2023)"
type: source
sources: [S2]
updated: 2026-11-23
---

# S2 — ReAct: Synergizing Reasoning and Acting in Language Models

- 原文：https://arxiv.org/abs/2210.03629（ICLR 2023）
- 閱讀筆記：`raw/02-yao-2022-react.md`
- 定位：「思考 → 行動 → 觀察」agent 迴圈的經典原始論文。

## 一句話摘要

讓 LLM 交錯產生推理與行動，推理幫助決定行動，行動帶回的資訊再幫助推理 [S2]。

## 重點

- 方法與格式 → [ReAct](../concepts/react.md)
- 通用迴圈概念 → [Agent 迴圈](../concepts/agent-loop.md)
- 只推理不行動的問題 → [挑戰與風險](../concepts/challenges-and-risks.md)

## 實驗結果

- HotpotQA（問答）與 FEVER（事實查核）：透過簡單的 Wikipedia API 取得資訊，改善只用 chain-of-thought 時的幻覺與錯誤傳遞 [S2]。
- ALFWorld 與 WebShop（互動決策）：只給 1–2 個範例，成功率比模仿學習與強化學習方法絕對提升 34% 與 10% [S2]。
- 推理軌跡讓人看得懂模型的決策過程，提升可解釋性與可信度 [S2]。
