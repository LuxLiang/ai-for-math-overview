# AI for Math Overview

[![Validate catalogue](https://github.com/LuxLiang/ai-for-math-overview/actions/workflows/catalogue.yml/badge.svg)](https://github.com/LuxLiang/ai-for-math-overview/actions/workflows/catalogue.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Capabilities, infrastructure, and mathematical contribution attribution.**

理解 AI4Math 的能力边界、关键基础设施与开放问题，重点关注数学证明中的知识依赖和贡献归因：一个结果解决了什么问题，证明继承了什么，以及真正新增的数学内容在哪里。

[能力现状](docs/landscape.md) · [基础设施](docs/infrastructure.md) · [贡献归因](docs/contribution-attribution.md) · [研究缺口](docs/research-gaps.md) · [项目索引](docs/resources.md) · [论文](docs/readings.md)

## Where AI4Math stands

| 研究环节 | 已有能力与代表性工作 | 仍需解决的问题 |
| --- | --- | --- |
| 解题与证明生成 | [DeepSeekMath V2](https://github.com/deepseek-ai/DeepSeek-Math-V2)、[Qwen2.5-Math](https://github.com/QwenLM/Qwen2.5-Math)：数学推理、自验证与工具使用 | 研究问题中的长程依赖、可靠验证，以及输出与已有文献的关系 |
| 形式化证明 | [Lean / Mathlib](https://github.com/leanprover-community/mathlib4)、[DeepSeek-Prover V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2)、[Goedel-Prover V2](https://github.com/Goedel-LM/Goedel-Prover-V2)：在给定形式化陈述下生成可检查证明 | 自然语言陈述的忠实性、数学库覆盖，以及形式化依赖与思想来源之间的映射 |
| 数学与算法发现 | [AlphaTensor](https://github.com/google-deepmind/alphatensor)、[FunSearch](https://github.com/google-deepmind/funsearch)、[AlphaEvolve](https://deepmind.google/blog/alphaevolve-impact/)：在可评价的搜索空间发现算法与构造 | 缺少自动评价器的开放问题，以及发现结果的贡献判定 |
| 非形式化证明审阅 | [OSVerify](https://arxiv.org/html/2610.18089v1#S3)：围绕具体疑点组织错误搜索与验证 | 审阅覆盖率、漏检、领域迁移与有限专家时间的分配 |
| 数学内容溯源 | [math-lineage](https://github.com/jnshi/math-lineage)：将具体结果、技巧与先前文献建立对应 | 从局部对应扩展到整条证明的依赖与新颖性分析 |

这些环节已有可复用的工具与研究实例；它们提供的证据不同。证明通过检查，支持的是陈述正确性；新颖性还需要对照既有文献。详细实验条件与适用范围见[能力现状](docs/landscape.md)。

## Infrastructure map

| 层次 | 代表性基础设施 | 对贡献归因的作用 |
| --- | --- | --- |
| 文献获取与标识 | [arXiv](https://info.arxiv.org/help/api/index.html)、[Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)、[OpenAlex](https://help.openalex.org/) | 找到候选前作，固定文献版本与时间关系 |
| 文档结构化 | [GROBID](https://github.com/grobidOrg/grobid)、[MinerU](https://github.com/opendatalab/MinerU) | 提取正文、公式、定理编号与参考文献，保留原文位置 |
| 数学知识与证明接口 | [Mathlib](https://github.com/leanprover-community/mathlib4)、[LeanDojo](https://github.com/lean-dojo/LeanDojo)、[Pantograph](https://github.com/stanford-centaur/PyPantograph) | 检索和验证形式化数学中的局部依赖 |
| 审阅与内容对应 | [OSVerify](https://github.com/OSVerify/OSVerify)、[math-lineage](https://github.com/jnshi/math-lineage) | 检查局部疑点，积累当前证明与先前工作的对应证据 |
| 评测与研究语料 | [miniF2F](https://github.com/facebookresearch/miniF2F)、[PutnamBench](https://github.com/trishullab/PutnamBench)、[SorryDB](https://github.com/SorryDB/SorryDB)、[OpenAI Math](https://github.com/openai/math) | 分别提供竞赛证明、真实项目任务与研究手稿；用途不混用 |

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

必须区分**论证缺口**和**创新性连接**：缺少证明的跳步首先是待验证义务，不能直接记作贡献。检索不到前作的步骤也应保留为未决。[完整分析框架 →](docs/contribution-attribution.md)

## Research direction

在本索引覆盖的代表性系统中，证明生成、错误检查和文献检索已经各自形成工具链。下一步值得检验的是：能否将它们组织成**可复核的证明依赖与贡献证据**。

```mermaid
flowchart LR
    A[论文与版本] --> B[主张和证明依赖]
    B --> C[候选前作检索]
    C --> D[局部对应与论证检查]
    D --> E[贡献判断与未决项]
    E --> F[专家复核]
```

这是拟研究的工作流。优先问题包括：证明步骤的稳定划分、跨论文符号与假设对齐、routine 判断，以及在有限审阅成本下识别真正需要专家判断的连接。[研究缺口与评测设计 →](docs/research-gaps.md)

## Scope

项目按技术代表性、社区使用、可复用性和研究关联度选择。同一路线合并历史版本；项目首页保留基础设施和代表性方法。OSVerify 与 math-lineage 作为贡献归因的专题案例单列，收录不意味着它们已形成领域共识。

[收录标准与证据口径](docs/methodology.md) · [Contributing](CONTRIBUTING.md) · [License](LICENSE)
