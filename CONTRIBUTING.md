# 贡献与维护

欢迎补充仓库、论文、技术文章与来源修正。每个 PR 请说明收录理由，提供原始来源，并核对它与现有条目是否重复。

1. 仓库条目编辑 `data/repositories.json`；论文与文章编辑 `data/readings.json`。
2. 使用现有分类、完整 HTTPS 链接、简短中文说明和 `YYYY-MM-DD` 核对日期。论文日期为首次提交或期刊发布日期。
3. 模型、代码、数据、部分组件与第三方实现请准确区分；未确认的资源不标为完整开放。
4. 论文 `repository` 填写已收录仓库的规范 `id`，没有明确关联时用 `null`。
5. 运行 `python3 scripts/build.py`，提交更新后的生成文档，再运行 `python3 scripts/build.py --check`。
6. PR 中说明来源核对、实际运行或复现分别做到了哪一步。

分类键：`foundation`、`formal`、`geometry`、`reasoning`、`discovery`、`benchmarks`。

`references.bib` 只提供标题、年份与入口链接，便于检索。正式论文引用请从上游获取包含作者、版本、会议或期刊信息的完整 BibTeX。
