# Selected Projects

[Overview](../README.md) · [Infrastructure](infrastructure.md) · [Selection criteria](methodology.md)

保留各层具有代表性和可复用性的项目。每个入口说明它解决的环节、收录理由和对贡献归因的边界。同一路线的历史版本不另起条目。

## Mathematical foundations

| 项目 | 角色与收录理由 | 能力边界 |
| --- | --- | --- |
| [Lean 4](https://github.com/leanprover/lean4) | **形式化证明的语言与检查内核**。多个证明器共享的基础；当前工具链含 lake check 与 lake comparator。 | 检查指定形式化目标和公理，不直接认证自然语言原意或历史新颖性。 |
| [Mathlib](https://github.com/leanprover-community/mathlib4) | **可复用的形式化数学知识库**。社区数学库，决定大量 Lean 任务的现成知识覆盖。 | 库中定理依赖不等于论文思想的历史来源。 |
| [Lean Blueprint](https://github.com/PatrickMassot/leanblueprint) | **作者标注的非形式化与形式化证明依赖图**。在大型 Lean 形式化项目中使用的证明规划和依赖展示工具。 | 图由作者使用标记组织，不能当作自动恢复任意论文证明结构。 |

## Literature and document processing

| 项目 | 角色与收录理由 | 能力边界 |
| --- | --- | --- |
| [GROBID](https://github.com/grobidOrg/grobid) | **文献结构与参考文献解析**。成熟的学术文档结构化基础设施。 | 参考文献解析不识别证明技术依赖。 |
| [MinerU](https://github.com/opendatalab/MinerU) | **PDF、版面与公式提取**。广泛使用的复杂文档结构化工具。 | 公式、编号和阅读顺序仍需与原页核对。 |
| [TheoremSearch / TheoremGraph](https://github.com/uw-math-ai/TheoremSearch) | **陈述级检索、候选依赖图与形式化匹配**。研究级数学检索与图结构的代表性基础设施；同一项目族合并收录。 | 候选依赖和语义匹配需要验证，引用恢复实验不等于历史新颖性判定。 |

## Formal theorem proving

| 项目 | 角色与收录理由 | 能力边界 |
| --- | --- | --- |
| [LeanDojo](https://github.com/lean-dojo/LeanDojo) | **证明环境、数据提取、前提检索**。检索增强定理证明的代表性开放框架；后续版本合并在此。 | 主要面向形式化语料；不直接恢复非形式化论文的证明谱系。 |
| [Pantograph](https://github.com/stanford-centaur/PyPantograph) | **程序化证明状态交互**。代表证明助手与外部搜索系统之间的接口层。 | 证明状态与 tactic 轨迹需要映射回人可读的数学步骤。 |
| [DeepSeek-Prover V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2) | **子目标分解与形式化证明生成**。具有公开模型和方法论文的代表性证明器。 | 基准证明成功率不度量新颖性和历史贡献。 |
| [Goedel-Prover V2](https://github.com/Goedel-LM/Goedel-Prover-V2) | **数据合成与验证反馈自纠正**。开放形式化证明训练路线的代表性工作。 | 训练与搜索的既有知识使用仍需单独记录。 |

## Mathematical reasoning

| 项目 | 角色与收录理由 | 能力边界 |
| --- | --- | --- |
| [DeepSeekMath V2](https://github.com/deepseek-ai/DeepSeek-Math-V2) | **自然语言证明生成与自验证**。数学推理从答案奖励走向证明级自验证的代表案例。 | 模型的自验证意见仍需独立证据。 |
| [Qwen2.5-Math](https://github.com/QwenLM/Qwen2.5-Math) | **数学模型与工具集成推理**。开放数学专用模型的代表性基线。 | 适合控制实验，但不能替代研究级文献归因。 |
| [NeMo-Skills](https://github.com/NVIDIA-NeMo/Skills) | **数学数据生成、训练和评测配方**。覆盖数据到评测的系统性开放研究工作流。 | 数据可追踪性不自动给出数学思想的来源。 |

## Mathematical and algorithmic discovery

| 项目 | 角色与收录理由 | 能力边界 |
| --- | --- | --- |
| [AlphaGeometry 2](https://github.com/google-deepmind/alphageometry2) | **几何符号推理**。神经符号几何路线的代表性后续系统。 | 公开仓库是 DDAR 核心与示例，完整神经系统不在此。 |
| [FunSearch](https://github.com/google-deepmind/funsearch) | **程序搜索与数学构造**。LLM 驱动数学发现的代表性方法。 | 需要可执行评价器，发现构造后的贡献判定另做。 |
| [AlphaTensor](https://github.com/google-deepmind/alphatensor) | **强化学习搜索矩阵乘法算法**。算法发现的标志性案例，有发现结果和验证材料。 | 公开算法材料与完整训练系统需要区分。 |

## Informal verification

| 项目 | 角色与收录理由 | 能力边界 |
| --- | --- | --- |
| [OSVerify](https://github.com/OSVerify/OSVerify)（专题案例） | **面向专家审阅的错误提议与验证**。研究任务直接相关；作为重点方法案例收录。 | 通过筛选并不证明正确，也不判断数学新颖性。 |

## Contribution attribution

| 项目 | 角色与收录理由 | 能力边界 |
| --- | --- | --- |
| [math-lineage](https://github.com/jnshi/math-lineage)（专题案例） | **数学技巧与前人工作的对应**。直接分析具体数学内容的历史来源与引用状态。 | 有限案例，报告由代理生成且通常未经人工核验。 |

## 评测基准与研究材料

| 项目 | 角色与收录理由 | 能力边界 |
| --- | --- | --- |
| [miniF2F](https://github.com/facebookresearch/miniF2F) | **形式化竞赛数学基准**。形式化竞赛数学的基础跨系统基准。 | 适合证明搜索对比，不能覆盖研究级原创性。 |
| [PutnamBench](https://github.com/trishullab/PutnamBench) | **大学竞赛形式化证明基准**。检验复杂形式化证明的代表性基准。 | 题目版本、证明提示与计算预算影响可比性。 |
| [SorryDB](https://github.com/SorryDB/SorryDB) | **真实 Lean 仓库任务**。把评测从固定竞赛题推进到真实未完成证明。 | 真实证明任务仍不等价于新定理发现。 |
| [MATH](https://github.com/hendrycks/math) | **自然语言数学解题基准**。数学模型研究的基础评测资源。 | 最终答案评测不能识别证明创新。 |
| [OpenAI Math](https://github.com/openai/math) | **研究手稿与证明材料**。研究级模型输出的集中分析语料，适合研究验证和归因。 | 各项验证状态不同，输出集合不等于独立的新结果清单。 |
| [NaturalProofs](https://github.com/wellecks/naturalproofs) | **非形式化数学前提检索数据与基准**。基础性数学参考结果检索任务，可作为溯源检索对照。 | 已有引用关系不等于历史首创标签；跨领域迁移须另测。 |
