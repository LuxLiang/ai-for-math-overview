# Selected Readings

[Overview](../README.md) · [Related work](related-work.md) · [Contribution attribution](contribution-attribution.md) · [Research gaps](research-gaps.md)

## Research focus

- **论证与内容比较**：IATC、BEq+、SAE / ACE 与 FaithAlign，核对联合前提、上下文与“同一数学内容”的定义。
- **贡献提取近邻**：Mathematical Instruments 和后续 Reusable Reasoning，按实际读取范围比较与目标的重叠。
- **检索与结构**：NaturalProofs、TheoremSearch / TheoremGraph、Matlas 和 Lean Blueprint，区分候选依赖、引用恢复和数学贡献判断。
- **局部验证**：[OSVerify §3](https://arxiv.org/html/2610.18089v1#S3)，理解分解、提议和验证的任务边界。
- **文献对应**：[math-lineage](https://github.com/jnshi/math-lineage)，查看证据位置、关系分类与实际报告。
- **新颖性近邻**：PriorProof、Beyond Correctness 与 Proof Perplexity，比较路线信号、判定管线、步骤非平凡性和实际评测。
- **研究过程**：Aletheia、First Proof 与 Data for Mathematical Copilots，核对人工贡献、研究工作流与评价目标。
- **宏观归因**：Who Solved It?，仅依据公开摘要讨论聚合与文献依赖问题。

下列论文按技术路线组织。arXiv 日期为首次提交日期；原始实验条件与结果应以论文为准。新颖性相关预印本用于近邻工作比较，其成熟度与基础设施项目分开评估。

## Literature and document processing

| 日期 | 文献 | 研究关联 |
| --- | --- | --- |
| 2026-02-05 | [Semantic Search over 9 Million Mathematical Theorems](https://arxiv.org/abs/2602.05216) | 陈述级语义检索，服务于定位候选前作，而非自动新颖性裁决。 |
| 2026-04-19 | [Matlas: A Semantic Search Engine for Mathematics](https://arxiv.org/abs/2604.17484) | 重点读 §3：依赖抽取与展开，为历史论文、教材中的结果提供检索入口。 |
| 2026-06-24 | [TheoremGraph: Bridging Formal and Informal Mathematics](https://arxiv.org/abs/2606.25363) | 重点读 §3–5 和附录 G：候选依赖、跨形式匹配及引用恢复实验。 |

## Formal theorem proving

| 日期 | 文献 | 研究关联 |
| --- | --- | --- |
| 2023-06-27 | [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](https://arxiv.org/abs/2306.15626) | 理解证明环境、前提检索和 ReProver 的关系。 |
| 2024-06-11 | [Reliable Evaluation and Benchmarks for Statement Autoformalization](https://arxiv.org/abs/2406.07222) | BEq+、ProofNetVerif 与研究级陈述评测；比较指标与历史归因分别评价。 |
| 2024-10-28 | [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://arxiv.org/abs/2410.20936) | 符号等价与语义一致性用于选择形式化候选；NeurIPS 2024 代表工作。 |
| 2025-04-30 | [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition](https://arxiv.org/abs/2504.21801) | 研究复杂定理的子目标分解与强化学习。 |
| 2025-08-05 | [Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction](https://arxiv.org/abs/2508.03613) | 研究分阶段数据生成和编译器反馈自纠正。 |
| 2025-11-12 | [Olympiad-level formal mathematical reasoning with reinforcement learning](https://www.nature.com/articles/s41586-025-09833-y) | AlphaProof 方法论文；论文公开不代表训练系统和权重完整开放。 |
| 2026-07-02 | [Leanstral 1.5: Proof Abundance for All](https://mistral.ai/news/leanstral-1-5/) [官方文章] | 后续模型版本介绍；文章保留不表示实验 API 仍可用。 |
| 2026-10-13 | [Aligning Faithfulness for Theory-Scale Autoformalization](https://arxiv.org/html/2610.18498v1) | 在上下文下对齐自然语言与形式化片段，定位不忠实或不可判定内容；非历史归因。 |
| 2026-10-18 | [Structure-Aware Equivalence for Evaluating Autoformalized Statements](https://arxiv.org/html/2610.25018v3) | 区分结构保持与整句逻辑等价；有限证明搜索未决不能当作不等价，近期预印本。 |

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
| 2018-03-17 | [Argumentation theory for mathematical argument](https://arxiv.org/abs/1803.06500) | 数学对象、推断、策略和论证结构的历史建模基础；不等于自动新颖性判定。 |
| 2024-12-19 | [Data for Mathematical Copilots: Better Ways of Presenting Proofs for Machine Learning](https://arxiv.org/abs/2412.15184) | 从数学工作流与非平凡重复讨论证明数据设计，为局部任务与标签提供方法背景。 |
| 2026-02-10 | [Towards Autonomous Mathematics Research](https://arxiv.org/abs/2602.10177) | 重点读 §3.3 与 §5：区分文献识别、重新发现、新结果及人工贡献。 |
| 2026-07-18 | [PriorProof: A Point-in-Time Measure of Technique Novelty for Formal Proofs](https://arxiv.org/abs/2607.16997) | 形式化路线非典型性信号；作者明确其不构成原创性检测，并讨论连接级新颖性盲点。 |
| 2026-08-02 | [Beyond Correctness: Toward Automated Novelty Verification with Lean 4](https://arxiv.org/abs/2608.14669) | 已有新颖性判定管线及有限实验；需关注未触发分支、自匹配与陈述忠实性。 |
| 2026-10-12 | [What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics](https://arxiv.org/abs/2610.17090) | 直接提取 AI 论文中的数学工具并比较前作；与本目标明显重叠，判断暂定且未独立认证。 |
| 2026-10-13 | [Who Solved It? Aggregation Bias and the Empty-Library Paradox in OpenAI's 722-Manuscript Mathematics Release](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7607840) | 聚合偏差与文献依赖的宏观讨论；当前仅依据可访问摘要，不将其统计当作因果归因证据。 **仅摘要。** |
| 2026-10-15 | [Proof Perplexity: A Probabilistic Approach to Measuring non-triviality in Machine Generated Proofs](https://arxiv.org/abs/2610.22612) | 直接研究步骤可恢复性与非平凡性；探索性度量，需审查分布假设、代理变量与外部验证。 |
| 2026-10-21 | [From Mathematical Instruments to Reusable Reasoning: A Second Phase of Extraction from AI-Generated Mathematics](https://zenodo.org/records/23523260) | 公开描述与来源推断图直接相关；PDF 403，仅读公开描述，未核对全文或实现。 **仅公开描述。** |

## 评测基准与研究材料

| 日期 | 文献 | 研究关联 |
| --- | --- | --- |
| 2021-03-24 | [NaturalProofs: Mathematical Theorem Proving in Natural Language](https://arxiv.org/abs/2104.01112) | 参考结果检索和生成的基础任务；可检验前提找回能力。 |
| 2021-08-31 | [MiniF2F: a cross-system benchmark for formal Olympiad-level mathematics](https://arxiv.org/abs/2109.00110) | 了解跨形式化语言的竞赛证明基准。 |
| 2024-07-15 | [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://arxiv.org/abs/2407.11214) | 考察比基础竞赛题更复杂的形式化证明任务。 |
| 2024-11-07 | [FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI](https://arxiv.org/abs/2411.04872) | 理解研究级数学问题评测；题库并非全部公开。 |
| 2025-02-12 | [One Example Shown, Many Concepts Known! Counterexample-Driven Conceptual Reasoning in Mathematical LLMs](https://arxiv.org/abs/2502.10454) | 反例推理的相关诊断任务；有效性与历史新颖性必须分别评价。 |
| 2025-05-21 | [MIRB: Mathematical Information Retrieval Benchmark](https://arxiv.org/abs/2505.15585) | 按陈述、答案、前提与公式分别评价检索；不能用相关性分数替代新颖性。 |
| 2026-02-05 | [First Proof](https://arxiv.org/abs/2602.05192) | 研究级证明的专家评价与学术规范；不是自动贡献归因基准。 |
| 2026-03-03 | [SorryDB: Can AI Provers Complete Real-World Lean Theorems?](https://arxiv.org/abs/2603.02668) | 了解从真实数学项目提取动态证明任务的方法。 |
