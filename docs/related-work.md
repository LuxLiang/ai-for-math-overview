# Related Work: From Retrieval to Contribution Attribution

[Overview](../README.md) · [Task coverage](task-coverage.md) · [Research gaps](research-gaps.md)

数学贡献归因已有相关的数据、检索系统、依赖图和探索性判定方法。研究定位需要逐层比较，不能把组件缺失和组件尚未可靠组合混为一谈。

## 1. Mathematical reference and theorem retrieval

| 代表工作 | 已有任务或产物 | 对本研究的作用 | 需要区分的边界 |
| --- | --- | --- | --- |
| [NaturalProofs](https://arxiv.org/abs/2104.01112) · [代码与数据](https://github.com/wellecks/naturalproofs) | 根据数学主张检索证明中使用的参考结果，并研究参考序列生成 | 前提检索与已有依赖找回的基础对照 | 数据中的引用不是历史首创标签，也未穷尽所有可行证明依赖 |
| [TheoremSearch](https://arxiv.org/abs/2602.05216) · [服务](https://www.theoremsearch.com/) | 面向数学陈述的语义检索 | 找到可能覆盖当前步骤的定理或引理 | 检索相关性不能直接说明假设满足或结果包含关系 |
| [Matlas](https://arxiv.org/html/2604.17484v1#S3) · [服务](https://matlas.ai/) | 从期刊和教材提取陈述及局部依赖，再展开上下文用于检索 | 补充 arXiv 之外的前作与背景条件 | 依赖展开是检索表示，不构成完整证明检查或首创性裁决 |
| [MIRB](https://arxiv.org/abs/2505.15585) | 将陈述、答案、前提与公式检索分别评价 | 选择与任务相符的检索基准 | 找到相关内容、找齐必需前提和识别原创贡献是不同目标 |

因此，文献侧不能只比较普通 RAG 与网页搜索；至少需要纳入陈述级检索和已有数学前提任务。不同语料范围与可访问条件必须记录。

## 2. Dependency graphs already exist

**Lean Blueprint 是可复用的组织工具。** [上游文档](https://github.com/PatrickMassot/leanblueprint)使用作者填写的 `\uses` 建立依赖，通过 `\lean` 对应形式化声明。它适合组织专家确认的证明结构；不能将其展示能力当作自动恢复未知论文全部依赖的结果。

**TheoremGraph 已经直接覆盖候选结构与跨文献匹配。** [论文 §3–5](https://arxiv.org/html/2606.25363v1#S3)包含非形式化候选依赖、Lean 声明图以及语义匹配。不同来源的边具有不同证据强度，不能统一视为已确认的逻辑依赖。§3 的边质量评估以独立 LLM 判断为参照，不能改称人工专家验证。

尤其相关的是[附录 G](https://arxiv.org/html/2606.25363v1)：作者遮掉真实段落中的引用，测试恢复对应论文及定理。其报告中图检索优于纯稠密检索的部分设置，但没有超过开放网页搜索；搜索预算未匹配，网页基线也可能找回原始被遮盖文本。因此它提供近邻任务和比较对象，尚不能直接评价未引用的技巧来源或新的证明连接。

上述观察意味着：**“构建证明依赖图”本身不足以成为研究新颖性主张。** 更具体的问题是哪些边正确、哪些关键边缺失，以及边上的推导关系如何支持贡献判断。

## 3. Novelty, non-triviality, and route variation

| 工作 | 实际测量或尝试 | 尚不能混同的目标 |
| --- | --- | --- |
| [PriorProof §6–7](https://arxiv.org/html/2607.16997v1#S6) | 用历史形式化依赖构造路线非典型性信号 | 作者明确区分该信号与原创性，并指出定义和连接级新颖性的盲点 |
| [Beyond Correctness / AViD Journal §4–6](https://arxiv.org/html/2608.14669v1#S4) | 组合重复检索、自动 tactic 和证明距离，已有管线及有限实验 | 不能称它“完全没有尝试新颖性判断”；但部分分支未获评测，语义忠实性和自匹配会影响结论 |
| [Proof Perplexity](https://arxiv.org/html/2610.22612v1) | 研究证明步骤的可恢复性与非平凡性，包含案例分析 | 概率及库相对信号需要检验其假设，不能直接解释为领域原创贡献比例 |

这些属于近邻研究，并不因为切中问题就自动成为成熟基础设施。比较时应明确：相对某个库难以恢复、形式化路线少见、数学上存在新连接和历史上没有先例，分别是什么构念。

## 4. Informal verification and content lineage

[OSVerify §3](https://arxiv.org/html/2610.18089v1#S3)提供分层错误提议与验证；[math-lineage](https://github.com/jnshi/math-lineage)提供内容对应、重要性与引用状态。它们是局部检查和溯源的接入点。

两者与依赖图、陈述检索结合后，还需检验：某条连接是否真由前作覆盖；若未直接覆盖，是标准推导、实质改造、新连接还是未完成义务。这个分类必须有可复核依据，且允许未决。

## 5. Research practice and expert evaluation

[Aletheia §3.3 与 §5](https://arxiv.org/html/2602.10177v1)区分文献识别、重新发现和新结果，并将人工参与程度与数学意义分开讨论。它提供归因分类和审阅实例，并非已经自动完成这些评价的证据。

[First Proof](https://1stproof.org/)提供研究级证明的专家评价背景；[Data for Mathematical Copilots](https://arxiv.org/html/2412.15184v2)强调数学工作流、局部任务和数据限制。后续评测应比较专家识别出的数学增量，而不能仅将题目答对作为贡献归因成功。

历史背景也值得保留：[Colton、Bundy、Walsh（2000）](https://cgi.cse.unsw.edu.au/~twalsh/IJHCS00.pdf)已讨论自动数学发现中的新颖性与有趣性。不能把这些概念的提出当作当前研究的创新。

## 6. Screening and evidence scope

本轮检索时间为 2026-10-25，覆盖数学前提检索、陈述级搜索、依赖抽取、形式/非形式匹配、引用恢复、证明路线差异、非平凡性、自动新颖性判定，以及研究级专家评价。检索同时沿代表论文的相关工作和引用继续追踪；这是一轮范围检索，不声称穷尽文献或满足系统综述协议。

采用的关键词组包括 `mathematical novelty attribution`、`proof dependency extraction`、`theorem retrieval`、`citation recovery`、`proof route diversity`、`routine / non-triviality` 和 `mathematical interestingness`。描述以原始论文、维护者文档、作者网页为依据，不以新闻摘要或项目自称“首次”作为能力证据。

| 筛选结果 | 处理方式 |
| --- | --- |
| NaturalProofs、Lean Blueprint、TheoremSearch / TheoremGraph | 加入项目索引；按技术作用收录，同一项目族合并 |
| Matlas、MIRB、Aletheia、First Proof、Data for Mathematical Copilots | 加入技术分析和论文索引；服务没有确认的上游代码时不虚构 GitHub 仓库 |
| PriorProof、AViD Journal、Proof Perplexity | 保留为直接近邻，明确探索性与评测边界 |
| [AIMing 作者页面](https://haielab.org/projects/aiming/)中的 NaturalPRISM、LeanRoute-216 相关工作 | 与中间证明状态检索、路线差异有关；页面标注 forthcoming，当前只核对作者介绍，作为后续追踪线索，不提升为成熟基础设施 |
| 轻量 MCP 包装器、个人演示、重复复现、来源不明的派生数据 | 不加入精选项目清单 |
| SSRN 7607840 | 仍为摘要层面的阅读，未获得全文，不新增其统计结论 |

本轮读取了 TheoremGraph 的方法、验证与附录 G，Matlas 的方法节，Aletheia 的分类讨论，PriorProof 的解释与局限，AViD Journal 的评测及局限，以及 Proof Perplexity 的方法和局限。没有运行这些系统，也没有把自动评审或作者报告当作独立专家验证。

## Research implication

已有工作覆盖的内容比“只有生成和查错”更广。可检验的研究定位应收窄为：**在完整主证明的关键连接上，对沿用、routine、实质改造、新连接和未完成义务提供可复核的定性证据。** 是否构成新的方法贡献，还要与上述近邻的完整实现、评测任务和专家标签进行比较。
