---
title: Augmented LLM（增強型 LLM）
type: concept
sources: [S3]
updated: 2026-11-23
---

# Augmented LLM（增強型 LLM）

## 定義

Agentic 系統的基本積木：一個 LLM 加上**檢索、工具、記憶**等增強能力；現在的模型會自己產生搜尋關鍵字、挑選工具、決定要記住什麼 [S3]。

## 實作重點

- 依使用情境量身打造這些能力 [S3]。
- 給 LLM 一個簡單、文件清楚的介面 [S3]。
- 一種做法是透過 Model Context Protocol（MCP）接上第三方工具 [S3]。

## 和 S1 三元件的關係

S1 的「規劃、記憶、工具」與 S3 的「檢索、工具、記憶」高度重疊；差別在 S3 把它定位成「積木」，要放進 workflow 或 agent 才變成完整系統 [整理]。

## 相關頁面

- [AI Agent 的定義](ai-agent-definition.md)
- [工具使用](tool-use.md)
- [記憶](memory.md)

## 來源

- [S3](../sources/s3-anthropic-bea.md)
