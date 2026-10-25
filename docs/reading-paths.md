# 按目标选择阅读路线

[返回主页](../README.md) · [完整论文索引](readings.md)

## 先建立领域认识

先区分自然语言解题、形式化证明、自动形式化与数学发现，再选择路线。理解基础概念后，可用一个熟悉的数学题对照：让模型给出自然语言证明，手动写成 Lean 陈述，再检查二者是否表达同一个命题。

Lean 入门建议使用上游教材：[Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/) 与 [Theorem Proving in Lean 4](https://lean-lang.org/theorem_proving_in_lean4/)。使用项目指定的 Lean 与 Mathlib 版本。

## 路线一：搭建形式化证明代理

1. **Lean + Mathlib + REPL**：理解定理、tactic、证明状态与编译器反馈，手工完成一个小证明。
2. **LeanDojo / Pantograph**：理解 Python 如何读写证明状态，如何区分超时、编译错误与证明成功。
3. **ReProver → DeepSeek-Prover V1.5 / V2 → Goedel-Prover V2**：比较前提检索、逐步搜索、整段证明生成和自纠正。
4. **miniF2F → PutnamBench → SorryDB**：从静态竞赛题扩展到真实仓库任务，记录具体数据版本与训练隔离方式。
5. **Lean Copilot / llmstep / UlamAI / MerLean**：观察交互式辅助与多步骤代理的实际工作流。

建议产物：固定一个小测试集，保存输入陈述、模型输出、Lean 日志、总调用次数与耗时。不要只保存成功样例。

## 路线二：数学推理模型与训练

1. **DeepSeekMath**：重点读数学数据选择与 GRPO。
2. **Qwen2.5-Math / ToRA**：比较纯文本推理和工具集成推理。
3. **DeepSeek-R1**：研究强化学习、蒸馏和推理行为。
4. **DeepSeekMath V2**：研究证明生成与自验证，明确自然语言验证器的能力边界。
5. **MATH / OlympiadBench / Math-Verify**：搭建答案抽取与评测流程，保留无法解析的输出。

建议产物：在同一个数据快照和采样预算下比较方法，分别统计答案正确率、解析失败率和工具成本。

## 路线三：数学发现与算法搜索

1. **Advancing mathematics by guiding human intuition with AI**：理解模型发现模式与人类数学解释之间的分工。
2. **AlphaTensor**：把算法问题转为可搜索的数学表示，检查公开算法与验证材料。
3. **FunSearch**：理解“程序候选 → 可执行评价器 → 选择与变异”的循环。
4. **Generative Modeling for Mathematical Discovery**：观察适合数学研究者使用的搜索实现。
5. **AlphaEvolve 官方文章 → OpenEvolve**：先理解原方法，再阅读明确标注的第三方实现。

建议产物：选择能精确计算评分的小问题，例如有限组合构造；复核最优候选，记录评价器、随机种子与搜索预算。有限搜索结果、数值证据与一般数学证明分别报告。

## 路线四：追踪研究前沿

从 [SorryDB](https://github.com/SorryDB/SorryDB) 的真实证明任务、[OpenAI Math](https://github.com/openai/math) 的研究材料，以及论文索引中的 Leanstral、AlphaEvolve 和大型自动形式化案例出发。

阅读时记录：原始问题、形式化陈述、验证方式、人工参与、公开代码/权重/数据和适用条件。新手稿的收录表示它值得跟踪；其具体数学主张应依据原文与验证材料逐项评估。
