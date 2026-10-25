# Contributing

贡献应帮助回答三个问题：AI4Math 已具备什么能力、哪些基础设施可以复用、数学贡献归因还存在什么问题。

## Add or update a resource

请提供上游链接、该项目所代表的技术环节、收录理由和能力边界。优先补充具有影响力的代表性工作；同一路线合并版本，避免增加功能重复的工具。

项目元数据位于 `data/repositories.json`。`tier` 区分代表项目与专题案例，`selection_reason_zh` 说明收录依据，`limitation_zh` 记录适用范围。论文数据位于 `data/readings.json`，`reading_scope` 记录实际读取范围；仅阅读摘要时必须明确标注。

## Update research analysis

README 与研究文档直接维护。区分作者报告、独立核对、实际复现和研究设想。有关数学新颖性、引用遗漏或证明错误的判断，应提供两侧具体位置，并说明复核状态；未经核验的候选不作为事实标签。

## Validate

```bash
python3 scripts/build.py
python3 scripts/build.py --check
```

脚本只生成项目索引、阅读索引和 `references.bib`；不会覆盖 README 和研究分析。检查包括元数据唯一性、关联项目、生成文件一致性及本地文档链接。

`references.bib` 是检索入口。正式引用请采用上游完整作者、版本、会议或期刊信息。
