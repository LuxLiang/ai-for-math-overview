# AI4Math Infrastructure

[Overview](../README.md) · [Projects](resources.md) · [Contribution attribution](contribution-attribution.md)

基础设施按研究流程划分。同一组件可以支持多个任务；这里关心它能为“这一步来自哪里、新在哪里”提供什么证据。

## 1. Literature and document ingestion

| 组件 | 提供什么 | 需要补上的部分 |
| --- | --- | --- |
| [arXiv](https://info.arxiv.org/help/api/index.html) | 文献标识、版本信息及可用全文入口 | 跟踪实际阅读版本；模型输出的日期不等于知识首次公开日期 |
| [Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) / [OpenAlex](https://help.openalex.org/) | 元数据、DOI 解析及学术关系检索入口 | 确认元数据指向同一作品；文献级关系还需细化到数学内容 |
| [GROBID](https://github.com/grobidOrg/grobid) | 从学术 PDF 提取结构和参考文献 | 将结构位置与具体定理、公式和证明用途连接 |
| [MinerU](https://github.com/opendatalab/MinerU) | 复杂文档的版面、文本与公式提取 | 核对符号、编号和跨页关系；保留与原文的对应 |

建议优先使用可获得的 TeX/HTML，PDF 作为原始证据保留。提取结果应记录文献版本、页码或环境标签、文件摘要和解析失败项；这属于拟议证据接口，不能假定上述工具已经统一输出。

## 2. Mathematical knowledge and proof interaction

| 组件 | 成熟的用途 | 对归因的局限 |
| --- | --- | --- |
| [Lean 4](https://github.com/leanprover/lean4) + [Mathlib](https://github.com/leanprover-community/mathlib4) | 编码数学陈述并复用形式化定理 | 内核检查支持正确性；形式化库引用不能完整恢复历史思想来源 |
| [LeanDojo](https://github.com/lean-dojo/LeanDojo) | 证明数据提取、前提选择和环境交互 | 形式化前提可能比论文中的概念步骤更细；[v2](https://github.com/lean-dojo/LeanDojo-v2) 属于同一技术谱系 |
| [Pantograph](https://github.com/stanford-centaur/PyPantograph) | 通过程序接口操作证明状态 | 需要额外建立 tactic 轨迹与人类可读证明结构的映射 |
| [LeanSearch](https://leansearch.net/) | 按自然语言检索 Mathlib 定理 | 命中相关定理不意味着确认了文献首创者或精确的假设适用性 |
| [DeepSeek-Prover V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2) / [Goedel-Prover V2](https://github.com/Goedel-LM/Goedel-Prover-V2) | 在给定任务下生成和修复形式化证明 | 生成一条可检查的新证明文本，不直接判定结果或方法的新颖性 |

LeanDojo 与 Pantograph分别代表数据/检索框架和证明交互接口；二者按层次比较，避免把同类包装器都加入清单。

## 3. Informal verification

[OSVerify](https://github.com/OSVerify/OSVerify)代表面向非形式化证明和论文的审阅路线。其研究论文侧重“错误提议—错误验证”；当前软件还提供文献检索与证据读取接口。软件能力应按提交版本检查，不能把仓库后续实现视为论文实验本身。

[文献工具文档](https://github.com/OSVerify/OSVerify/blob/c43385bcbedec943cabe0d7e95df5b50404d9acb/docs/literature-tools.md)描述了候选文献搜索、引用解析和带位置的原文读取。它为文献审阅提供可借鉴的证据接口，但并不输出完整的贡献依赖图。全文分段和数学依赖结构也需要区别处理。

## 4. Provenance and attribution

[math-lineage](https://github.com/jnshi/math-lineage)直接研究数学内容与前人工作的对应，提供报告和机器可读结果。其关系分类区分相同结果、相同技巧、改造、部分复用、既有路线、较弱前作及证明捷径；另记录重要性和引用状态。[分类定义](https://github.com/jnshi/math-lineage/blob/da8c0e694f00c2575ccf9d26c0ea560543ef0a1b/.agents/skills/precedence-review/references/scope-and-relationships.md)

这提供了**局部内容对应的实例**。扩展到后续研究时，还需覆盖已正确引用的步骤、标准推导和检索未决项；否则只能看到被发现的引用问题，无法解释整篇论文的贡献结构。

## 5. Evaluation and corpora

| 资源 | 适合检验 | 不适合直接检验 |
| --- | --- | --- |
| [MATH](https://github.com/hendrycks/math) | 自然语言数学解题 | 研究证明的新颖性 |
| [miniF2F](https://github.com/facebookresearch/miniF2F) / [PutnamBench](https://github.com/trishullab/PutnamBench) | 固定陈述下的形式化证明 | 对前人工作的贡献归因 |
| [SorryDB](https://github.com/SorryDB/SorryDB) | 真实项目中的未完成证明 | 从问题发现到新结果的全部过程 |
| [OpenAI Math](https://github.com/openai/math) | 手稿、验证材料及其对应关系 | 未经逐项核对的新颖性标签 |
| [math-lineage 报告](https://github.com/jnshi/math-lineage#reviewed-preprints) | 内容对应格式和检索案例 | 直接充当人工金标准；项目说明报告通常未经人工核验 |

## Reuse versus research

| 可以从现有组件开始 | 需要进一步建立和验证 |
| --- | --- |
| 文献获取、解析、标识和版本管理 | 证明中主张与推导边的稳定表示 |
| 形式化环境交互和局部检查 | 跨论文假设、结论和符号的语义对齐 |
| 候选文献检索与具体疑点检查 | routine、实质改造和新连接的专家标注协议 |
| 局部溯源报告格式 | 覆盖整条证明、保留未决项的贡献分析与评测集 |

这里列的是本研究目标下的接入边界。具体系统是否覆盖其中某一子问题，应通过其文档、案例和运行结果核对。
