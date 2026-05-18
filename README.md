# 工程设计方法论 · Engineering Design Methodology

## 在线访问

https://conanxin.github.io/Engineering_Design_Methodology_docs/

## 这是什么

这是一个将早期工程设计方法学学习笔记整理为现代 GitHub Pages 工具站的项目。

当前版本不再只是 Sphinx 文档归档，而是面向工程方案、产品设计、知识库建设与本地 Agent 工作流的工程设计方法论站点。

## 它解决什么问题

- 把模糊想法转成任务书
- 区分必达要求与愿望
- 建立功能结构
- 生成方案矩阵
- 做技术设计检查
- 做成本与风险估算
- 将方法论转成 Hermes / OpenClaw Agent 工作流

## 内容结构

- 使用指南
- 十章方法论
- 案例库
- 图解
- 模板库
- 概念索引
- Agent 工作流
- 更新日志

## 如何使用

**初学者路径**：从引言开始，逐步阅读十章方法论。

**项目实践路径**：直接进入案例库与模板库，结合自己的项目拆解。

**Agent 工作流路径**：查看 Agent 工作流页面，将方法论转化为可执行指令。

## 仓库结构

- `docs/` — GitHub Pages 发布目录
- `modernization/site/` — 现代化站点源文件
- `modernization/templates/` — 方法论模板
- `modernization/hermes_skill_draft/` — Hermes skill 草案（实验）
- `modernization/docs/` — 阶段报告与说明文档
- `unit*.rst` — 历史 Sphinx 文档源文件（保留）
- `conf.py` / `Makefile` — 历史 Sphinx 构建配置（保留）

## 历史来源

本仓库最初是使用 Sphinx / reStructuredText 整理《工程设计学》相关学习笔记的早期文档项目。原始 `.rst` 文件仍完整保留，作为历史资料与 source archive。

## 版权与引用边界

- 原始笔记源自早期学习整理。
- 现代化页面以摘要、重写、结构化导航、案例化转译和个人方法论解释为主。
- 不将本站内容视为原书替代品。
- 真实工程方案仍需专业人员复核。

## 当前状态

**Phase 2 complete**：
- GitHub Pages 站点已上线
- 首页、章节页、案例库、模板库、概念索引、Agent 工作流已完成
- 移动端、SEO、sitemap、robots、404、changelog、分享封面图已完成
- 主站 projects 索引已接入

## 后续路线

- Phase 3：Hermes skill 正式化
- 深化真实案例
- 增加更多工程图解
- 将方法论接入本地 Agent 日常工作流
