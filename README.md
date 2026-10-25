# AI for Math Overview

[![Validate catalogue](https://github.com/LuxLiang/ai-for-math-overview/actions/workflows/catalogue.yml/badge.svg)](https://github.com/LuxLiang/ai-for-math-overview/actions/workflows/catalogue.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Capabilities, infrastructure, and mathematical contribution attribution.**

理解 AI4Math 的能力边界、关键基础设施与开放问题，重点关注数学证明中的知识依赖和贡献归因：一个结果解决了什么问题，证明继承了什么，以及真正新增的数学内容在哪里。

[证明案例](docs/huang-sensitivity-case.md) · [任务定义](docs/task-specification.md) · [近邻重叠审查](docs/overlap-audit.md) · [任务覆盖](docs/task-coverage.md) · [研究缺口](docs/research-gaps.md)

[相关工作](docs/related-work.md) · [能力现状](docs/landscape.md) · [基础设施](docs/infrastructure.md) · [项目索引](docs/resources.md) · [论文](docs/readings.md)

## Task coverage: Mathematical Contribution Attribution

以一篇论文为输入，目标是解释主证明的结构、对既有工作的依赖，以及结果与证明分别新增了什么。下表比较本索引已核对的代表性工作；“有局部能力”不表示该环节已经可靠解决。

| 目标 | 现有工作做到哪里 | 相对本研究目标的缺口 |
| --- | --- | --- |
| 表示证明结构 | Lean Blueprint 可组织作者标注的依赖；TheoremGraph 已抽取候选陈述依赖 | 核对结构的正确性、完整性和适合贡献判断的粒度 |
| 找到既有结果 | NaturalProofs 有前提检索任务；TheoremSearch、Matlas 提供陈述级检索 | 验证候选结果的假设与结论是否真正覆盖当前步骤 |
| 恢复文献来源 | TheoremGraph 附录 G 已做引用恢复实验；math-lineage 输出内容对应 | 从已有引用找回扩展到未引用技巧、间接来源和整条主证明 |
| 检查关键跳跃 | OSVerify 可检查疑点，现有检索和依赖图能提供线索 | 分别核对来源、条件、改造、routine 补全依据与论证状态，允许多个判断并存 |
| 判断证明非平凡性 | PriorProof、Proof Perplexity 已研究相对库的路线和步骤信号 | 验证信号是否对应专家认可的数学增量 |
| 对齐数学内容 | BEq+、SAE / ACE、FaithAlign 已研究陈述或片段的比较 | 明确比较对象；整句互相可证不能自动代表同一数学结果 |
| 提取贡献候选 | Mathematical Instruments 已提取证明机制并比较前作；后续来源图工作与目标直接重叠 | 与近邻同条件比较准确性、覆盖和专家复核，不能把输出贡献图本身视为创新 |
| 区分新颖性与过程贡献 | AViD Journal 已尝试新颖性管线；Aletheia 讨论结果与人工参与分类 | 分别评估结果、证明、场景与反例，保留来源和未决项 |

研究定位需要建立在这些已有能力之上。新增近邻、读取范围和重叠结论见[近邻审查](docs/overlap-audit.md)；可复核的判断单位与诊断案例见[任务定义](docs/task-specification.md)。

## Infrastructure map

| 层次 | 代表性基础设施 | 对贡献归因的作用 |
| --- | --- | --- |
| 文献获取与标识 | [arXiv](https://info.arxiv.org/help/api/index.html)、[Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)、[OpenAlex](https://help.openalex.org/) | 找到候选前作，固定文献版本与时间关系 |
| 文档结构化 | [GROBID](https://github.com/grobidOrg/grobid)、[MinerU](https://github.com/opendatalab/MinerU) | 提取正文、公式、定理编号与参考文献，保留原文位置 |
| 数学知识与证明接口 | [Mathlib](https://github.com/leanprover-community/mathlib4)、[LeanDojo](https://github.com/lean-dojo/LeanDojo)、[Pantograph](https://github.com/stanford-centaur/PyPantograph) | 检索和验证形式化数学中的局部依赖 |
| 陈述检索与候选依赖 | [TheoremSearch / TheoremGraph](https://www.theoremsearch.com/)、[Matlas](https://matlas.ai/)、[Lean Blueprint](https://github.com/PatrickMassot/leanblueprint) | 提供陈述检索、候选图或作者标注的结构；其证据强度需要区分 |
| 审阅与内容对应 | [OSVerify](https://github.com/OSVerify/OSVerify)、[math-lineage](https://github.com/jnshi/math-lineage) | 检查局部疑点，积累当前证明与先前工作的对应证据 |
| 评测基准与研究材料 | [miniF2F](https://github.com/facebookresearch/miniF2F)、[PutnamBench](https://github.com/trishullab/PutnamBench)、[SorryDB](https://github.com/SorryDB/SorryDB)、[OpenAI Math](https://github.com/openai/math) | 分别提供竞赛证明、真实项目任务与研究手稿；用途不混用 |

工具的输入输出、可复用部分和接入后的空缺见[基础设施分析](docs/infrastructure.md)。

## Mathematical contribution attribution

核心分析单位是**一个数学主张及其推导依赖**。整篇论文的引用数量或模型的自述，都不足以回答哪些部分是新贡献。

| 问题 | 需要的证据 |
| --- | --- |
| **结果新在哪里？** | 与前作逐项比较对象、假设、结论、参数范围；区分新结果、推广、反例与重述 |
| **证明新在哪里？** | 对齐关键引理、构造和证明路线，区分直接使用、改造与新的连接 |
| **关键跳跃在哪里？** | 找出前提到结论之间必须新增的论证，检查前作能否直接补齐 |
| **哪些属于 routine？** | 给定领域与前提，说明能用哪些标准结果推得；由领域专家核对 |
| **贡献由谁完成？** | 记录人、模型、工具与文献的实际作用；仅有文本相似性不能确定生成过程 |

来源、routine、正确性与新颖性分别记录。一段论证可以复用旧方法、包含新改造，又留有待证明义务；检索不到前作的步骤保留为未决。[完整分析框架 →](docs/contribution-attribution.md)

## Research direction

在本索引覆盖的代表性系统中，证明生成、文献检索、候选依赖和局部审阅已经有可复用工作。下一步值得检验的是：能否将它们组织成**可复核的证明依赖与贡献证据**。

```mermaid
flowchart LR
    A[论文与版本] --> B[主张与联合前提推断]
    B --> C[候选前作检索]
    C --> D[局部对应与论证检查]
    D --> E[贡献判断与未决项]
    E --> F[专家复核]
```

首个[真实证明案例](docs/huang-sensitivity-case.md)已拆解 Huang 的敏感度定理，核对前作中的弱界、上界构造及参数界，并对照 Mathlib 的替代证明路线。案例将“给定构造后的验证”与“构造及用途的发现”分别记录，附有可重复的有限数学检查；独立专家复核与模型比较尚待开展。[研究缺口与评测设计 →](docs/research-gaps.md)
