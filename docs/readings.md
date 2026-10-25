# 论文与技术文章

[返回主页](../README.md) · [阅读路线](reading-paths.md)

论文标题与日期优先取自 arXiv 原始元数据或期刊页面；arXiv 使用首次提交日期。官方博客单独列出。每项的核对日期保存在[结构化数据](../data/readings.json)。下列导读是阅读提示，不是独立复现实验结论。

## 形式化证明与自动形式化

| 日期 | 论文 | 阅读重点 | 关联仓库 |
| --- | --- | --- | --- |
| 2023-06-27 | [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](https://arxiv.org/abs/2306.15626) | 理解证明环境、前提检索和 ReProver 的关系。 | [lean-dojo/LeanDojo](https://github.com/lean-dojo/LeanDojo) |
| 2023-10-27 | [LLMSTEP: LLM proofstep suggestions in Lean](https://arxiv.org/abs/2310.18457) | 了解轻量的 Lean tactic 建议接口。 | [wellecks/llmstep](https://github.com/wellecks/llmstep) |
| 2024-04-18 | [Lean Copilot: Large Language Models as Copilots for Theorem Proving in Lean](https://arxiv.org/abs/2404.12534) | 了解编辑器中的语言模型证明辅助。 | [lean-dojo/LeanCopilot](https://github.com/lean-dojo/LeanCopilot) |
| 2024-08-15 | [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://arxiv.org/abs/2408.08152) | 研究强化学习、证明反馈与树搜索。 | [deepseek-ai/DeepSeek-Prover-V1.5](https://github.com/deepseek-ai/DeepSeek-Prover-V1.5) |
| 2024-10-21 | [Pantograph: A Machine-to-Machine Interaction Interface for Advanced Theorem Proving, High Level Reasoning, and Data Extraction in Lean 4](https://arxiv.org/abs/2410.16429) | 了解可交互证明环境如何支持自动搜索。 | [stanford-centaur/PyPantograph](https://github.com/stanford-centaur/PyPantograph) |
| 2025-02-11 | [Goedel-Prover: A Frontier Model for Open-Source Automated Theorem Proving](https://arxiv.org/abs/2502.07640) | 理解合成形式化数据的作用。 | [Goedel-LM/Goedel-Prover](https://github.com/Goedel-LM/Goedel-Prover) |
| 2025-04-15 | [Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning](https://arxiv.org/abs/2504.11354) | 研究大规模形式化推理模型的训练。 | [MoonshotAI/Kimina-Prover-Preview](https://github.com/MoonshotAI/Kimina-Prover-Preview) |
| 2025-04-30 | [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition](https://arxiv.org/abs/2504.21801) | 研究复杂定理的子目标分解与强化学习。 | [deepseek-ai/DeepSeek-Prover-V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2) |
| 2025-08-05 | [Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction](https://arxiv.org/abs/2508.03613) | 研究分阶段数据生成和编译器反馈自纠正。 | [Goedel-LM/Goedel-Prover-V2](https://github.com/Goedel-LM/Goedel-Prover-V2) |
| 2025-11-12 | [Olympiad-level formal mathematical reasoning with reinforcement learning](https://www.nature.com/articles/s41586-025-09833-y) | AlphaProof 方法论文；论文公开不代表训练系统和权重完整开放。 | — |

## 几何推理

| 日期 | 论文 | 阅读重点 | 关联仓库 |
| --- | --- | --- | --- |
| 2024-01-17 | [Solving olympiad geometry without human demonstrations](https://www.nature.com/articles/s41586-023-06747-5) | 理解神经辅助点生成与符号几何推导。 | [google-deepmind/alphageometry](https://github.com/google-deepmind/alphageometry) |
| 2025-02-05 | [Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2](https://arxiv.org/abs/2502.03544) | 研究几何符号引擎与辅助点生成如何配合。 | [google-deepmind/alphageometry2](https://github.com/google-deepmind/alphageometry2) |

## 自然语言数学推理与工具使用

| 日期 | 论文 | 阅读重点 | 关联仓库 |
| --- | --- | --- | --- |
| 2023-09-29 | [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://arxiv.org/abs/2309.17452) | 研究自然语言推理和代码执行如何交替。 | [microsoft/ToRA](https://github.com/microsoft/ToRA) |
| 2024-02-05 | [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) | 了解数学预训练与 GRPO 的起点。 | [deepseek-ai/DeepSeek-Math](https://github.com/deepseek-ai/DeepSeek-Math) |
| 2024-09-18 | [Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement](https://arxiv.org/abs/2409.12122) | 了解中英文数学模型与工具集成推理。 | [QwenLM/Qwen2.5-Math](https://github.com/QwenLM/Qwen2.5-Math) |
| 2025-01-22 | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) | 了解推理强化学习与模型蒸馏。 | [deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) |
| 2025-11-27 | [DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning](https://arxiv.org/abs/2511.22570) | 区分自然语言证明自验证与形式化内核验证。 | [deepseek-ai/DeepSeek-Math-V2](https://github.com/deepseek-ai/DeepSeek-Math-V2) |

## 数学发现与算法搜索

| 日期 | 论文 | 阅读重点 | 关联仓库 |
| --- | --- | --- | --- |
| 2021-12-01 | [Advancing mathematics by guiding human intuition with AI](https://www.nature.com/articles/s41586-021-04086-x) | 机器学习寻找结构与模式，由数学家解释并形成数学结果。 | — |
| 2022-10-05 | [Discovering faster matrix multiplication algorithms with reinforcement learning](https://www.nature.com/articles/s41586-022-05172-4) | 从张量分解和强化学习理解算法发现。 | [google-deepmind/alphatensor](https://github.com/google-deepmind/alphatensor) |
| 2023-12-14 | [Mathematical discoveries from program search with large language models](https://www.nature.com/articles/s41586-023-06924-6) | 从程序生成、演化与可计算评价器理解构造搜索。 | [google-deepmind/funsearch](https://github.com/google-deepmind/funsearch) |
| 2025-03-14 | [Generative Modeling for Mathematical Discovery](https://arxiv.org/abs/2503.11061) | 了解为数学家设计的 FunSearch 实现与构造搜索。 | — |

## 数据集、基准与评测工具

| 日期 | 论文 | 阅读重点 | 关联仓库 |
| --- | --- | --- | --- |
| 2021-03-05 | [Measuring Mathematical Problem Solving With the MATH Dataset](https://arxiv.org/abs/2103.03874) | 了解竞赛数学最终答案评测的基础数据。 | [hendrycks/math](https://github.com/hendrycks/math) |
| 2021-08-31 | [MiniF2F: a cross-system benchmark for formal Olympiad-level mathematics](https://arxiv.org/abs/2109.00110) | 了解跨形式化语言的竞赛证明基准。 | [openai/miniF2F](https://github.com/openai/miniF2F) |
| 2021-10-27 | [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168) | 了解应用题推理与验证器训练。 | [openai/grade-school-math](https://github.com/openai/grade-school-math) |
| 2023-02-24 | [ProofNet: Autoformalizing and Formally Proving Undergraduate-Level Mathematics](https://arxiv.org/abs/2302.12433) | 研究自然语言到形式化陈述的对齐。 | [zhangir-azerbayev/ProofNet](https://github.com/zhangir-azerbayev/ProofNet) |
| 2024-02-21 | [OlympiadBench: A Challenging Benchmark for Promoting AGI with Olympiad-Level Bilingual Multimodal Scientific Problems](https://arxiv.org/abs/2402.14008) | 了解中英文多模态奥赛评测。 | [OpenBMB/OlympiadBench](https://github.com/OpenBMB/OlympiadBench) |
| 2024-07-15 | [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://arxiv.org/abs/2407.11214) | 考察比基础竞赛题更复杂的形式化证明任务。 | [trishullab/PutnamBench](https://github.com/trishullab/PutnamBench) |
| 2024-11-07 | [FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI](https://arxiv.org/abs/2411.04872) | 理解研究级数学问题评测；题库并非全部公开。 | — |
| 2026-03-03 | [SorryDB: Can AI Provers Complete Real-World Lean Theorems?](https://arxiv.org/abs/2603.02668) | 了解从真实数学项目提取动态证明任务的方法。 | [SorryDB/SorryDB](https://github.com/SorryDB/SorryDB) |
| 2026-04-08 | [Riemann-Bench: A Benchmark for Moonshot Mathematics](https://arxiv.org/abs/2604.06802) | 补充研究级数学的私有基准视角。 | — |

## 官方文章与项目进展

| 日期 | 文章 | 阅读重点 |
| --- | --- | --- |
| 2026-09-04 | [Formalizing Fermat's Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem) | 大型数学证明自动形式化案例；结合原始陈述、依赖与检查方式阅读。 |
| 2026-07-02 | [Leanstral 1.5: Proof Abundance for All](https://mistral.ai/news/leanstral-1-5/) | 后续模型版本介绍；文章保留不表示实验 API 仍可用。 |
| 2026-05-07 | [AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields](https://deepmind.google/blog/alphaevolve-impact/) | 官方后续进展，帮助追踪数学构造与算法发现方向。 |
| 2026-03-16 | [Leanstral: Open-Source foundation for trustworthy vibe-coding](https://mistral.ai/news/leanstral/) | Lean 形式化推理模型的官方介绍；在线 API 的现状应另查更新日志。 |
| 2025-05-14 | [AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) | 官方方法介绍：程序演化与自动评价；第三方 OpenEvolve 应独立标注。 |
| 2024-07-25 | [AI achieves silver-medal standard solving International Mathematical Olympiad problems](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/) | 了解 AlphaProof 与 AlphaGeometry 2 的任务分工及竞赛实验背景。 |
