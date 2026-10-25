# AI for Math Overview

A curated overview of AI for mathematics: repositories, papers, articles, and reading paths. 中文导读，保留原始英文项目名与论文标题。

**首版核对日期：2026-10-25 · 39 个仓库 · 30 篇论文 · 6 篇官方文章**

整理 AI 如何辅助数学解题、证明、形式化与发现。优先链接项目上游、作者论文和官方技术文章，每项附简短说明与核对日期。这是精选入门索引，覆盖经典路线与部分 2026 年进展，后续继续扩充。

## 导航

- [GitHub 仓库](#repositories)
- [论文与技术文章](docs/readings.md)
- [按研究目标选择阅读路线](docs/reading-paths.md)
- [收录标准与评测注意事项](docs/methodology.md)
- [贡献与维护](CONTRIBUTING.md)
- [结构化仓库数据](data/repositories.json) · [阅读数据](data/readings.json) · [精简 BibTeX](references.bib)

## 研究版图

| 方向 | 典型任务 | 主要反馈 |
| --- | --- | --- |
| 自然语言推理 | 解题、生成证明草稿、调用代码工具 | 最终答案比较、执行结果、自然语言审阅 |
| 形式化证明 | 在 Lean 等系统中补全可检查的证明 | 证明助手与内核检查 |
| 自动形式化 | 将数学陈述与推导转为形式化代码 | 编译反馈，以及人对原意的核对 |
| 几何推理 | 图形关系推导与辅助点搜索 | 符号几何推理器 |
| 数学发现 | 寻找构造、猜想、算法和反例 | 可计算目标、实验与后续数学证明 |

形式化证明验证的是所编码的陈述；仍需检查该陈述是否忠实表达原题、依赖哪些公理以及是否存在占位证明。最终答案正确与整段论证正确也应分别评估。详见[方法说明](docs/methodology.md)。

## 从哪里开始

1. **了解领域**：先读下方分类，再沿[阅读路线](docs/reading-paths.md)选一条主线。
2. **实现 Lean 证明代理**：Lean / Mathlib → LeanDojo 或 Pantograph → ReProver / DeepSeek-Prover → miniF2F / PutnamBench → SorryDB。
3. **研究数学模型训练**：DeepSeekMath → Qwen2.5-Math / ToRA → DeepSeek-R1 → DeepSeekMath V2。
4. **研究数学发现**：AI 引导数学直觉 → AlphaTensor → FunSearch → AlphaEvolve；用 OpenEvolve 研究第三方实现。

<a id="repositories"></a>

## GitHub 仓库

开放内容是阅读入口提示，不保证完整训练流程可复现。模型、数据和代码可能采用不同许可；以各组件上游许可为准。第三方实现单独标注，已归档仓库会保留历史价值并注明状态。

### 证明基础设施

| 项目 | 用途 | 开放内容 / 角色 |
| --- | --- | --- |
| [Lean 4](https://github.com/leanprover/lean4) | 交互式证明助手与内核，是许多 AI 形式化证明系统的验证基础。 | 基础设施 |
| [Mathlib](https://github.com/leanprover-community/mathlib4) | Lean 4 的社区数学库，支持定义、定理与证明复用。 | 数学库 |
| [Lean REPL](https://github.com/leanprover-community/repl) | 让外部程序与 Lean 证明环境交互的基础工具。 | 代码 |

### 形式化证明与自动形式化

| 项目 | 用途 | 开放内容 / 角色 |
| --- | --- | --- |
| [LeanDojo](https://github.com/lean-dojo/LeanDojo) | 提取 Lean 证明数据、交互环境与检索增强证明研究。 | 代码/数据 |
| [LeanDojo v2](https://github.com/lean-dojo/LeanDojo-v2) | 用于训练、评估和部署 Lean 4 AI 证明器的后续框架。 | 代码 |
| [ReProver](https://github.com/lean-dojo/ReProver) | 检索前提并生成证明步骤的 LeanDojo 配套证明器。 | 代码/模型 |
| [Lean Copilot](https://github.com/lean-dojo/LeanCopilot) | 在 Lean 编辑环境中提供证明步骤建议与证明搜索。 | 代码/模型 |
| [Pantograph](https://github.com/stanford-centaur/PyPantograph) | Python 与 Lean 4 证明状态交互，适合构建搜索环境。 | 代码 |
| [DeepSeek-Prover V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2) | 通过子目标分解与强化学习提升 Lean 形式化证明。 | 代码/模型 |
| [DeepSeek-Prover V1.5](https://github.com/deepseek-ai/DeepSeek-Prover-V1.5) | 结合强化学习与树搜索的早期开放证明器。 | 代码/模型 |
| [Goedel-Prover V2](https://github.com/Goedel-LM/Goedel-Prover-V2) | 研究脚手架式合成数据与自纠正的形式化证明训练。 | 代码/模型/数据 |
| [Goedel-Prover](https://github.com/Goedel-LM/Goedel-Prover) | 通过合成形式化数据训练开放 Lean 证明器。 | 代码/模型/数据 |
| [llmstep](https://github.com/wellecks/llmstep) | 在 Lean 中调用语言模型建议下一步 tactic。 | 代码 |
| [Kimina Lean Server](https://github.com/project-numina/kimina-lean-server) | 提供 Lean 代码批量验证服务与客户端 SDK。 | 代码 |
| [Kimina-Prover Preview](https://github.com/MoonshotAI/Kimina-Prover-Preview) | 研究大规模形式化推理与强化学习的开放预览。 | 代码/模型 |
| [UlamAI](https://github.com/ulamai/ulamai) | 开放 Lean 证明与自动形式化工作流，包含自然语言证明入口。 | 代码 |
| [MerLean](https://github.com/MerLeanProver/MerLean) | 基于规划图的 Lean 4 与 Mathlib 自动证明代理。 | 代码 |

### 几何推理

| 项目 | 用途 | 开放内容 / 角色 |
| --- | --- | --- |
| [AlphaGeometry](https://github.com/google-deepmind/alphageometry) | 神经生成与符号几何推导结合的竞赛几何系统。 | 代码/模型 |
| [AlphaGeometry 2](https://github.com/google-deepmind/alphageometry2) | 公开 DDAR 符号推理核心与示例；该仓库不包含完整神经生成系统。 | 部分代码：DDAR |

### 自然语言数学推理与工具使用

| 项目 | 用途 | 开放内容 / 角色 |
| --- | --- | --- |
| [DeepSeekMath](https://github.com/deepseek-ai/DeepSeek-Math) | 数学预训练、指令微调与 GRPO 的早期开放研究。 | 代码/模型 |
| [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) | 通用推理模型，在数学任务中研究强化学习与蒸馏。 | 模型/报告 |
| [Qwen2.5-Math](https://github.com/QwenLM/Qwen2.5-Math) | 支持中英文思维链与工具集成推理的数学模型系列。 | 代码/模型 |
| [ToRA](https://github.com/microsoft/ToRA) | 交替使用自然语言推理与程序工具解决数学问题。 | 代码/模型 |
| [Numina AIMO](https://github.com/project-numina/aimo-progress-prize) | 数学竞赛解题的训练、推理与工具使用材料。 | 代码 |
| [NeMo-Skills](https://github.com/NVIDIA-NeMo/Skills) | 包含数学推理数据生成、训练与评测工作流。 | 代码/配方 |
| [DeepSeekMath V2](https://github.com/deepseek-ai/DeepSeek-Math-V2) | 研究自然语言数学证明的生成与自验证。 | 模型/报告 |

### 数学发现与算法搜索

| 项目 | 用途 | 开放内容 / 角色 |
| --- | --- | --- |
| [FunSearch](https://github.com/google-deepmind/funsearch) | 语言模型生成程序，并用可计算目标筛选数学构造。 | 代码/示例 |
| [AlphaTensor](https://github.com/google-deepmind/alphatensor) | 以张量分解搜索矩阵乘法算法的官方研究材料。 | 算法/验证与基准代码 |
| [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve) | 受 AlphaEvolve 启发的第三方程序演化实现。 | 代码；第三方实现 |
| [OpenAI Math](https://github.com/openai/math) | 研究手稿与相关验证材料的发布入口，逐项查看验证状态。 | 研究材料 |

### 数据集、基准与评测工具

| 项目 | 用途 | 开放内容 / 角色 |
| --- | --- | --- |
| [miniF2F](https://github.com/openai/miniF2F) | 跨形式化语言的竞赛数学证明基准。 | 基准/数据；已归档 |
| [PutnamBench](https://github.com/trishullab/PutnamBench) | Putnam 竞赛题目的形式化证明基准。 | 基准/数据 |
| [ProofNet](https://github.com/zhangir-azerbayev/ProofNet) | 自然语言与形式化陈述配对，用于自动形式化。 | 基准/数据 |
| [MATH](https://github.com/hendrycks/math) | 自然语言竞赛数学题与解答，用于非形式化解题评测。 | 基准/数据 |
| [GSM8K](https://github.com/openai/grade-school-math) | 小学应用题多步推理基准，作为基础能力对照。 | 基准/数据；已归档 |
| [OlympiadBench](https://github.com/OpenBMB/OlympiadBench) | 包含奥赛数学与物理的中英文多模态基准。 | 基准/数据 |
| [Math-Verify](https://github.com/huggingface/Math-Verify) | 抽取和比较模型最终数学答案的工具。 | 评测工具 |
| [miniF2F (Meta)](https://github.com/facebookresearch/miniF2F) | Meta 维护的 miniF2F 相关版本；使用时与 OpenAI 原仓库区分并固定提交。 | 基准/数据 |
| [SorryDB](https://github.com/SorryDB/SorryDB) | 从真实 Lean 项目收集未完成证明任务，配套代理和验证工具。 | 基准/数据/代码 |

## 持续维护

条目来源与说明保存在 `data/`，展示文档由脚本生成，减少重复编辑：

```bash
python3 scripts/build.py          # 校验数据并生成文档
python3 scripts/build.py --check  # 校验数据与生成文件是否一致
```

只使用 Python 标准库。GitHub Actions 在推送和 PR 时运行离线一致性检查；不自动抓取、改写条目或发布未经审核的资源。增加内容请参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

本仓库原创说明和维护脚本采用 [MIT License](LICENSE)。链接指向的论文、代码、模型和数据各自遵循上游许可，本仓库不重新分发这些资源。
