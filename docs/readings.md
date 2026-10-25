# Selected Readings

[Overview](../README.md) · [Contribution attribution](contribution-attribution.md) · [Research gaps](research-gaps.md)

## Research focus

- **局部验证**：[OSVerify §3](https://arxiv.org/html/2610.18089v1#S3)，理解分解、提议和验证的任务边界。
- **文献对应**：[math-lineage](https://github.com/jnshi/math-lineage)，查看证据位置、关系分类与实际报告。
- **新颖性信号**：PriorProof 与 Beyond Correctness，比较形式化依赖、检索与专家判断。
- **宏观归因**：Who Solved It?，仅依据公开摘要讨论聚合与文献依赖问题。

下列论文按技术路线组织。arXiv 日期为首次提交日期；原始实验条件与结果应以论文为准。新颖性相关预印本用于近邻工作比较，其成熟度与基础设施项目分开评估。

## Formal theorem proving

| 日期 | 文献 | 研究关联 |
| --- | --- | --- |
| 2023-06-27 | [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](https://arxiv.org/abs/2306.15626) | 理解证明环境、前提检索和 ReProver 的关系。 |
| 2025-04-30 | [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition](https://arxiv.org/abs/2504.21801) | 研究复杂定理的子目标分解与强化学习。 |
| 2025-08-05 | [Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction](https://arxiv.org/abs/2508.03613) | 研究分阶段数据生成和编译器反馈自纠正。 |
| 2025-11-12 | [Olympiad-level formal mathematical reasoning with reinforcement learning](https://www.nature.com/articles/s41586-025-09833-y) | AlphaProof 方法论文；论文公开不代表训练系统和权重完整开放。 |
| 2026-07-02 | [Leanstral 1.5: Proof Abundance for All](https://mistral.ai/news/leanstral-1-5/) [官方文章] | 后续模型版本介绍；文章保留不表示实验 API 仍可用。 |

## Mathematical reasoning

| 日期 | 文献 | 研究关联 |
| --- | --- | --- |
| 2023-09-29 | [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://arxiv.org/abs/2309.17452) | 研究自然语言推理和代码执行如何交替。 |
| 2024-02-05 | [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) | 了解数学预训练与 GRPO 的起点。 |
| 2024-09-18 | [Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement](https://arxiv.org/abs/2409.12122) | 了解中英文数学模型与工具集成推理。 |
| 2025-01-22 | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) | 了解推理强化学习与模型蒸馏。 |
| 2025-11-27 | [DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning](https://arxiv.org/abs/2511.22570) | 区分自然语言证明自验证与形式化内核验证。 |

## Mathematical and algorithmic discovery

| 日期 | 文献 | 研究关联 |
| --- | --- | --- |
| 2021-12-01 | [Advancing mathematics by guiding human intuition with AI](https://www.nature.com/articles/s41586-021-04086-x) | 机器学习寻找结构与模式，由数学家解释并形成数学结果。 |
| 2022-10-05 | [Discovering faster matrix multiplication algorithms with reinforcement learning](https://www.nature.com/articles/s41586-022-05172-4) | 从张量分解和强化学习理解算法发现。 |
| 2023-12-14 | [Mathematical discoveries from program search with large language models](https://www.nature.com/articles/s41586-023-06924-6) | 从程序生成、演化与可计算评价器理解构造搜索。 |
| 2024-01-17 | [Solving olympiad geometry without human demonstrations](https://www.nature.com/articles/s41586-023-06747-5) | 理解神经辅助点生成与符号几何推导。 |
| 2025-02-05 | [Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2](https://arxiv.org/abs/2502.03544) | 研究几何符号引擎与辅助点生成如何配合。 |
| 2026-05-07 | [AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields](https://deepmind.google/blog/alphaevolve-impact/) [官方文章] | 官方后续进展，帮助追踪数学构造与算法发现方向。 |

## Informal verification

| 日期 | 文献 | 研究关联 |
| --- | --- | --- |
| 2026-10-13 | [One-Sided Verification Under Limited Expert Review](https://arxiv.org/html/2610.18089v1) | 重点读第 3 节：分层提出错误并单独验证；为步骤级研究提供方法参照。 |

## Contribution attribution

| 日期 | 文献 | 研究关联 |
| --- | --- | --- |
| 2026-07-18 | [PriorProof: A Point-in-Time Measure of Technique Novelty for Formal Proofs](https://arxiv.org/abs/2607.16997) | 以历史形式化依赖足迹构造证明路线信号；限定构念与专家判断的关系。 **仅摘要。** |
| 2026-08-02 | [Beyond Correctness: Toward Automated Novelty Verification with Lean 4](https://arxiv.org/abs/2608.14669) | 探索新颖性检查并讨论陈述忠实性、检索覆盖和复现障碍；初步研究。 **仅摘要。** |
| 2026-10-13 | [Who Solved It? Aggregation Bias and the Empty-Library Paradox in OpenAI's 722-Manuscript Mathematics Release](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7607840) | 聚合偏差与文献依赖的宏观讨论；当前仅依据可访问摘要，不将其统计当作因果归因证据。 **仅摘要。** |

## 评测基准与研究材料

| 日期 | 文献 | 研究关联 |
| --- | --- | --- |
| 2021-08-31 | [MiniF2F: a cross-system benchmark for formal Olympiad-level mathematics](https://arxiv.org/abs/2109.00110) | 了解跨形式化语言的竞赛证明基准。 |
| 2024-07-15 | [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://arxiv.org/abs/2407.11214) | 考察比基础竞赛题更复杂的形式化证明任务。 |
| 2024-11-07 | [FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI](https://arxiv.org/abs/2411.04872) | 理解研究级数学问题评测；题库并非全部公开。 |
| 2026-03-03 | [SorryDB: Can AI Provers Complete Real-World Lean Theorems?](https://arxiv.org/abs/2603.02668) | 了解从真实数学项目提取动态证明任务的方法。 |
