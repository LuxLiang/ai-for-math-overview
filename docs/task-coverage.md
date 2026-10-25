# Task Coverage: Mathematical Contribution Attribution

[Overview](../README.md) · [Analysis protocol](contribution-attribution.md) · [Evaluation design](research-gaps.md)

## Target output

输入一篇数学论文及其可检索的前作，输出主证明的主张与依赖、每个关键连接的来源证据，以及结果新颖性和证明新颖性的定性判断。对新场景和反例分别检查。分析应能回答：前几步已知之后，下一步还需要完成什么数学工作？

覆盖判断基于代表性系统的论文、文档与一份实际输出的接口核对，尚未运行或系统评测这些工具。因此不把这里的缺口解释为整个领域不存在相关研究。

## Existing components

| 组件 | 已有可借鉴的能力 | 没有由这些证据建立的能力 |
| --- | --- | --- |
| [math-lineage](https://github.com/jnshi/math-lineage) | 当前内容与前作的具体位置对应；区分相同结果、技巧复用和实质改造等关系 | 对全文所有关键步骤的完整覆盖；对未匹配部分可靠确认新颖性 |
| [OSVerify](https://arxiv.org/html/2610.18089v1#S3) | 分解审阅、提出具体错误并验证它是否破坏论证 | 将所有推导边归类为已知、routine、改造或新连接 |
| [Lean / Mathlib](https://github.com/leanprover-community/mathlib4) | 在指定形式化环境中检查陈述、复用既有定理 | 历史来源、概念原创性，以及形式化陈述与原文的全部对应 |
| [PriorProof](https://arxiv.org/abs/2607.16997) | 基于历史形式化依赖的路线非典型性信号 | 通用论文的结果原创性、领域专家意义下的 routine 和过程归因 |

## What the actual output shows

核对的 math-lineage 实例为[一份已有报告的 JSON](https://github.com/jnshi/math-lineage/blob/da8c0e694f00c2575ccf9d26c0ea560543ef0a1b/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/precedence-findings.json)。其记录包含：

- `preprint_locations` 与来源 `locators`：两侧内容的位置。
- `relationship`：数学关系，而非只有文本相似度。
- `credit_status`：是否为这项具体内容给予引用。
- `centrality`：主结果、关键、支撑或外围等重要性判断。
- `attribution_gap` 与 `overstated_novelty`：按其规则组织的报告标记。

这说明它已超出普通参考文献推荐，能够组织局部数学溯源证据。但该实例的核心结构是 findings 列表，不能直接读出完整主证明的所有节点、推导边及未审阅部分。项目还明确排除特定形式的教科书材料，因此不宜把报告中没有出现的内容当作新贡献。[范围定义](https://github.com/jnshi/math-lineage/blob/da8c0e694f00c2575ccf9d26c0ea560543ef0a1b/.agents/skills/precedence-review/references/scope-and-relationships.md)

这些记录由代理生成，本仓库没有独立确认其中的具体数学归因。它们在这里证明的是输出格式和分析范围，不是数学结论已经正确。

OSVerify 的[输出协议](https://github.com/OSVerify/OSVerify/blob/c43385bcbedec943cabe0d7e95df5b50404d9acb/docs/output-contract.md)记录审阅范围、疑点、审核和完成状态。这里的覆盖指计划中的审阅流程；不能据此认定已经恢复了论文的数学依赖图，或完成贡献归因。

## The missing decision: 3 → 4

假设第 1–3 步已经由前作 A 覆盖。从第 3 步到第 4 步，必须逐项检验：

| 候选解释 | 需要补齐的证据 |
| --- | --- |
| 直接沿用前作 B | B 的明确位置；假设是否满足；结论是否覆盖第 4 步 |
| routine 推导 | 允许使用的标准结果，以及从第 3 步到第 4 步的具体推导 |
| 对既有方法的实质改造 | 旧方法在哪个条件下失效，修改了哪个核心步骤 |
| 新的关键连接 | 前作对照、充分论证与专家判断；检索范围必须保留 |
| 证明缺口 | 缺少的义务是什么；在补齐前保持未决，不能认定创新 |

“找到旧部分”已有接近可复用的组件；“在整条证明里解释剩下的数学增量”仍需要结构表示、条件核对、routine 协议和专家评测共同支撑。这里是基于已检查工作作出的研究判断。

## Status of this repository

| 工作 | 当前进度 | 还需要的证据 |
| --- | --- | --- |
| 代表性工作梳理 | 已完成项目、论文与能力边界整理 | 后续维护与补充近邻研究 |
| 接口核对 | 已查看一份实际溯源记录和审阅协议 | 实际运行后的质量、成本和覆盖率 |
| 任务定义 | 已提出结果、证明、场景、反例与过程的分维度协议 | 专家确认标签含义与适用粒度 |
| 完整真实案例 | 尚未完成 | 从论文主定理追溯到关键步骤和前作，逐条保留证据 |
| routine 与新连接判断 | 尚未评测 | 独立专家标注、分歧记录与模型对照 |
| 可运行归因系统 | 尚未实现 | 可复现流程、失败分析与基线比较 |

## Next deliverable

先完成一份真实论文的完整案例：主证明依赖图、关键边的来源对照、routine 的具体推导、候选新连接与未决项。随后由领域专家复核，并比较直接整篇判断与分步骤分析的差异。

成功标准是能可靠回答“数学增量在哪里、依据是什么”，包括必要时明确回答“目前无法判断”。不以步骤数量或引用数量给出贡献百分比。
