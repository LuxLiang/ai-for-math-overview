#!/usr/bin/env python3
"""Validate the catalogue and render Markdown/BibTeX using only stdlib."""
import argparse
import datetime
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'foundation': '证明基础设施',
    'formal': '形式化证明与自动形式化',
    'geometry': '几何推理',
    'reasoning': '自然语言数学推理与工具使用',
    'discovery': '数学发现与算法搜索',
    'benchmarks': '数据集、基准与评测工具',
}


def load():
    repos = json.loads((ROOT / 'data/repositories.json').read_text())
    readings = json.loads((ROOT / 'data/readings.json').read_text())
    for rows, fields in [(repos, {'id', 'name', 'url', 'category', 'description_zh', 'availability', 'source_role', 'checked_on', 'license', 'archived'}),
                         (readings, {'id', 'title', 'url', 'category', 'date', 'kind', 'note_zh', 'repository', 'checked_on'})]:
        seen_ids, seen_urls = set(), set()
        for row in rows:
            assert fields <= row.keys(), f'Missing fields: {row}'
            assert row['id'].lower() not in seen_ids, f'Duplicate ID: {row["id"]}'
            assert row['url'].lower() not in seen_urls, f'Duplicate URL: {row["url"]}'
            seen_ids.add(row['id'].lower())
            seen_urls.add(row['url'].lower())
            assert row['category'] in CATEGORIES
            parsed = urlparse(row['url'])
            assert parsed.scheme == 'https' and parsed.netloc
            datetime.date.fromisoformat(row['checked_on'])
    ids = {r['id'] for r in repos}
    for r in repos:
        assert r['url'] == 'https://github.com/' + r['id']
        assert r['source_role'] in {'upstream', 'third-party'}
        assert isinstance(r['archived'], bool)
    for p in readings:
        assert p['repository'] is None or p['repository'] in ids, p['repository']
        assert p['kind'] in {'paper', 'article'}
        assert datetime.date.fromisoformat(p['date']) <= datetime.date.fromisoformat(p['checked_on'])
    return repos, readings


def cell(text):
    return str(text).replace('|', '\\|').replace('\n', ' ')


def render(repos, readings):
    papers = [p for p in readings if p['kind'] == 'paper']
    articles = [p for p in readings if p['kind'] == 'article']
    readme = f'''# AI for Math Overview

A curated overview of AI for mathematics: repositories, papers, articles, and reading paths. 中文导读，保留原始英文项目名与论文标题。

**首版核对日期：2026-10-25 · {len(repos)} 个仓库 · {len(papers)} 篇论文 · {len(articles)} 篇官方文章**

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

'''
    for category, title in CATEGORIES.items():
        readme += f'### {title}\n\n| 项目 | 用途 | 开放内容 / 角色 |\n| --- | --- | --- |\n'
        for r in repos:
            if r['category'] != category:
                continue
            availability = r['availability']
            if r['source_role'] == 'third-party':
                availability += '；第三方实现'
            if r['archived']:
                availability += '；已归档'
            readme += f'| [{cell(r["name"])}]({r["url"]}) | {cell(r["description_zh"])} | {cell(availability)} |\n'
        readme += '\n'
    readme += '''## 持续维护

条目来源与说明保存在 `data/`，展示文档由脚本生成，减少重复编辑：

```bash
python3 scripts/build.py          # 校验数据并生成文档
python3 scripts/build.py --check  # 校验数据与生成文件是否一致
```

只使用 Python 标准库。GitHub Actions 在推送和 PR 时运行离线一致性检查；不自动抓取、改写条目或发布未经审核的资源。增加内容请参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

本仓库原创说明和维护脚本采用 [MIT License](LICENSE)。链接指向的论文、代码、模型和数据各自遵循上游许可，本仓库不重新分发这些资源。
'''
    doc = '# 论文与技术文章\n\n[返回主页](../README.md) · [阅读路线](reading-paths.md)\n\n'
    doc += '论文标题与日期优先取自 arXiv 原始元数据或期刊页面；arXiv 使用首次提交日期。官方博客单独列出。每项的核对日期保存在[结构化数据](../data/readings.json)。下列导读是阅读提示，不是独立复现实验结论。\n\n'
    for category, title in CATEGORIES.items():
        group = [p for p in papers if p['category'] == category]
        if not group:
            continue
        doc += f'## {title}\n\n| 日期 | 论文 | 阅读重点 | 关联仓库 |\n| --- | --- | --- | --- |\n'
        for p in sorted(group, key=lambda p: p['date']):
            repo = f'[{p["repository"]}](https://github.com/{p["repository"]})' if p['repository'] else '—'
            doc += f'| {p["date"]} | [{cell(p["title"])}]({p["url"]}) | {cell(p["note_zh"])} | {repo} |\n'
        doc += '\n'
    doc += '## 官方文章与项目进展\n\n| 日期 | 文章 | 阅读重点 |\n| --- | --- | --- |\n'
    for p in sorted(articles, key=lambda p: p['date'], reverse=True):
        doc += f'| {p["date"]} | [{cell(p["title"])}]({p["url"]}) | {cell(p["note_zh"])} |\n'
    bib = '% Minimal discovery references: title/year/URL only. Use upstream BibTeX for academic citation.\n\n'
    for p in readings:
        title = p['title'].replace('&', r'\&').replace('%', r'\%').replace('_', r'\_')
        key = 'aimath' + p['id'].replace('.', '').replace('-', '')
        bib += f'@misc{{{key},\n  title = {{{{{title}}}}},\n  year = {{{p["date"][:4]}}},\n  url = {{{p["url"]}}}\n}}\n\n'
    return {'README.md': readme, 'docs/readings.md': doc, 'references.bib': bib.rstrip() + '\n'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    repos, readings = load()
    for filename, content in render(repos, readings).items():
        path = ROOT / filename
        if args.check:
            assert path.exists() and path.read_text() == content, f'Regenerate {filename}'
        else:
            path.write_text(content)
    print(f'Validated {len(repos)} repositories and {len(readings)} readings; generated files are current.')


if __name__ == '__main__':
    main()
