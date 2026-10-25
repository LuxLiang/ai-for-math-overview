# Overlap Audit: What Would Be New?

[Overview](../README.md) · [Related work](related-work.md) · [Task specification](task-specification.md)

研究目标是定性解释数学贡献：给出主证明的关键推断、对既有工作的依赖，以及仍需新增的数学工作。下面记录与目标重叠的研究，避免把已有组件或输出格式当作方法贡献。比较依据是原始文献和文档，未运行系统或复现其测量。

## 1. Argument structure predates LLM proof agents

[Argumentation Theory for Mathematical Argument](https://arxiv.org/abs/1803.06500)提出 IATC，对数学对象、推断和策略等内容建模，并分析实际数学交流与论证实例。它比简单的“句子之间加依赖边”更接近解释证明思路，但不提供当前任务所需的自动历史新颖性判定。

对本研究的约束是：**区分陈述、推断和启发式策略已有先例**。需要检验的是自动提取与归因的可靠性，以及具体论证中省略的条件能否被恰当地恢复。

## 2. Mathematical instrument extraction is a close neighbor

[What the Machine Invented](https://arxiv.org/html/2610.17090v1)直接从 AI 数学手稿提取引理、构造和证明机制，比较前作并给出暂定的新颖性意见。这与“指出证明继承了什么、增加了什么”有实质重叠。作者也明确其新颖性判断受检索范围限制，未独立认证全部证明或历史优先权。

其后续 [From Mathematical Instruments to Reusable Reasoning](https://zenodo.org/records/23523260)的公开描述进一步提出带来源和范围的联合前提推断图。**当前仅读到 Zenodo 的公开描述；PDF 下载返回 403，未核对全文和实现。** 这个线索足以要求进一步比较，但不足以证明方法准确或结果可复现。

| 已有工作或近邻提出的内容 | 本研究不能直接声称的新颖点 | 仍可检验的问题 |
| --- | --- | --- |
| 提取数学工具、改造和新组合候选 | 首次从 AI 论文中提取数学贡献 | 相同来源、预算下，能否减少错误归因并识别遗漏的关键连接 |
| 把推断与前作位置相连 | 首次输出带来源的贡献图 | 来源对应是否满足适用条件，是否忠实说明剩余义务 |
| 以联合前提和范围组织推断 | 首次使用超图或范围标签 | 合取前提、分支和局部假设能否被可靠恢复并由专家复核 |

方法论文未充分评测一个问题，不等于它没有提出该问题；后续工作的区别需要落在可检验的方法或证据上。

## 3. Statement equivalence is not one operation

| 工作 | 已有能力或研究目标 | 与本任务的关系 |
| --- | --- | --- |
| [SymEq / Semantic Consistency](https://arxiv.org/abs/2410.20936) | 按符号与语义一致性选择形式化候选；NeurIPS 2024 工作 | 表达不同不应直接判为新结果，但候选间一致不保证忠于原文 |
| [BEq+ / ProofNetVerif](https://aclanthology.org/2025.emnlp-main.907/) | 参考形式化陈述的比较与人工标注基准；EMNLP 2025 工作 | 提供参照任务和数据，不能直接测历史新颖性 |
| [SAE / ACE v3](https://arxiv.org/html/2610.25018v3) | 保留数学角色的陈述关系，提供有限范围内的验证及未决输出 | 直接约束“同一个数学结果”的操作定义；属于近期预印本，尚未独立复现 |
| [FaithAlign](https://arxiv.org/html/2610.18498v1) | 在上下文下对齐自然语言与形式化片段，并标注忠实、缺陷或不可判定 | 可以借鉴局部证据组织；标注的不是两篇论文之间的历史归因 |
| [Lean 验证工具](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) | 对可信形式化挑战检查证明、陈述依赖与公理 | 支持形式化任务的一致性，不决定非形式化原意或历史首创 |

当前 Lean 文档已提供 `lake check` 和 `lake comparator`；旧 [comparator 仓库](https://github.com/leanprover/comparator)已归档并提示迁移。它作为 Lean 基础设施的一部分记录，不再重复加入一个过时的独立工具条目。

## 4. A logical-equivalence trap

在能证明 P 和 Q 的固定理论里，可以分别构造 P → Q 和 Q → P：忽略输入，使用已有的另一条证明。这不意味着 P 与 Q 在数学对象、假设、结论和解释上是同一个结果。

[SAE / ACE](https://arxiv.org/html/2610.25018v3)直接研究了相关的结构保持问题。对本研究，陈述对齐应同时检查对象、量词、假设角色和结论，不把无限制互相可证当作“已有同一结果”的充分条件。反过来，有限搜索没找到证明也不能据此断言不等价。

## 5. Counterexamples and process labels

[CounterMATH](https://arxiv.org/abs/2502.10454)可作为反例推理能力的相关任务。构造有效反例和证明它在历史上是新反例，需要分别评价；已有教材型反例任务不能直接提供原创性标签。此处只将其列为论文和诊断任务，不增加重复的精选仓库。

一般学术文献中的引用用途也已有成熟研究。例如 [SciCite](https://aclanthology.org/N19-1361/)区分背景、方法使用和结果比较等用途。但“用于方法”仍不足以证明某条数学推断的必要性、历史最早来源或新颖性，不能直接把引用用途标签改名为数学贡献标签。

## 6. Screening decisions

本次沿原论文的任务定义、方法、局限和引用继续检索，覆盖数学论证建模、陈述等价、上下文忠实性、贡献提取与反例。没有新增个人包装器或仅演示界面的项目。

| 线索 | 核对范围与处理 |
| --- | --- |
| IATC | 阅读作者存档的论文文本与实例；作为建模背景加入 |
| SymEq、BEq+ | 核对原始论文、发表信息及任务；作为陈述比较的代表工作加入 |
| SAE / ACE、FaithAlign | 阅读原始预印本的定义、评测和边界；作为直接近邻加入，非成熟通用判定器 |
| Mathematical Instruments | 阅读原文的方法与局限；作为必须比较的贡献提取近邻加入 |
| Reusable Reasoning | 仅公开描述可访问；全文与实现待核对，不采用其准确率或完整性主张 |
| NaturalPRISM / LeanRoute-216 | 仍仅核对作者页面，标为 forthcoming；不改变为已复现或成熟系统 |
| [Natural Language Premise Selection](https://arxiv.org/abs/2004.14959) | 较早的前提检索背景；与 NaturalProofs 同层，不另增精选项目 |
| [The Faithfulness Gap](https://arxiv.org/html/2606.16541v1) | 核对探针方法与局限；其结论有解释和探针标签等假设，不将“certifying”解读为无条件自然语言语义保证 |
| SciCite 引用用途分类 | 核对原论文摘要与任务；作为用途与数学依赖不同的背景，不增加主清单 |
| 一般论证挖掘、课堂原创性评分 | 可启发标注，但不直接迁移为研究数学的贡献金标准；不扩充为主清单 |

## Research decision

当前证据不支持把“贡献提取 + 来源图”本身作为新的研究定位。更具体的候选是：**在明确来源和上下文条件下，核对关键推断的适用性与剩余证明义务，并分别评价其来源、改造、routine 和正确性。** 是否有新的方法贡献，仍需同条件基线、独立专家案例和失败分析来确定。
