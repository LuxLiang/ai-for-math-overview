# AI for Math Overview

[![Validate catalogue](https://github.com/LuxLiang/ai-for-math-overview/actions/workflows/catalogue.yml/badge.svg)](https://github.com/LuxLiang/ai-for-math-overview/actions/workflows/catalogue.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Capabilities, infrastructure, and mathematical contribution attribution.**

理解 AI4Math 的能力边界、关键基础设施与开放问题，重点关注数学证明中的知识依赖和贡献归因：一个结果解决了什么问题，证明继承了什么，以及真正新增的数学内容在哪里。

[任务覆盖](docs/task-coverage.md) · [能力现状](docs/landscape.md) · [基础设施](docs/infrastructure.md) · [贡献归因](docs/contribution-attribution.md) · [研究缺口](docs/research-gaps.md) · [项目索引](docs/resources.md) · [论文](docs/readings.md)

## Task coverage: Mathematical Contribution Attribution

以一篇论文为输入，目标是解释主证明的结构、对既有工作的依赖，以及结果与证明分别新增了什么。下表比较本索引已核对的代表性工作；“有局部能力”不表示该环节已经可靠解决。

| 目标 | 现有工作做到哪里 | 相对本研究目标的缺口 |
| --- | --- | --- |
| 拆解主证明 | OSVerify 可以分段并围绕局部论证提出疑点 | 文本分段还需转为数学主张与推导依赖，且覆盖整条主证明 |
| 识别已知结果和技巧 | math-lineage 给出具体内容与前作的双侧位置、关系及引用状态 | 从选中的对应发现扩展到包括已充分引用内容在内的完整分析 |
| 检查 3 → 4 这样的跳跃 | OSVerify 可检查局部论证是否存在实质问题；math-lineage 可提供前作线索 | 联合判断它属于既有结果、routine、实质改造、新连接还是未完成义务 |
| 判断 routine | 标准库、自动 tactic 和形式化依赖提供可检查的局部信号 | 明确领域先验与粒度，验证这些信号是否符合专家的数学判断 |
| 区分结果与证明的新颖性 | math-lineage 区分结果/技巧关系；PriorProof 提供受限的证明路线信号 | 对新结果、新证明、新场景、反例分别建立证据和评测 |
| 解释整体贡献 | math-lineage 提供局部重要性标签 | 说明哪些连接支撑主定理，避免按未匹配步骤比例推断原创性 |

依据：[OSVerify §3](https://arxiv.org/html/2610.18089v1#S3)、[math-lineage](https://github.com/jnshi/math-lineage)、[PriorProof](https://arxiv.org/abs/2607.16997)。接口核对、适用范围和下一阶段交付物见[任务覆盖分析](docs/task-coverage.md)。

**本仓库进度**：已完成代表性工作整理、接口层面对照和研究问题定义；尚未完成真实论文的完整贡献分析、系统复现或专家评测。下一阶段需要用实际案例检验上述缺口，而非仅增加资源条目。

## Infrastructure map

| 层次 | 代表性基础设施 | 对贡献归因的作用 |
| --- | --- | --- |
| 文献获取与标识 | [arXiv](https://info.arxiv.org/help/api/index.html)、[Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)、[OpenAlex](https://help.openalex.org/) | 找到候选前作，固定文献版本与时间关系 |
| 文档结构化 | [GROBID](https://github.com/grobidOrg/grobid)、[MinerU](https://github.com/opendatalab/MinerU) | 提取正文、公式、定理编号与参考文献，保留原文位置 |
| 数学知识与证明接口 | [Mathlib](https://github.com/leanprover-community/mathlib4)、[LeanDojo](https://github.com/lean-dojo/LeanDojo)、[Pantograph](https://github.com/stanford-centaur/PyPantograph) | 检索和验证形式化数学中的局部依赖 |
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

## Contributors

- [LuxLiang](https://github.com/LuxLiang) — 项目发起与维护、研究方向和收录标准。
- **Codex (OpenAI)** — AI 协作贡献者，参与文献整理、研究文档撰写与仓库工具维护。

## Scope

项目按技术代表性、社区使用、可复用性和研究关联度选择。同一路线合并历史版本；项目首页保留基础设施和代表性方法。OSVerify 与 math-lineage 作为贡献归因的专题案例单列，收录不意味着它们已形成领域共识。

[收录标准与证据口径](docs/methodology.md) · [Contributing](CONTRIBUTING.md) · [License](LICENSE)
