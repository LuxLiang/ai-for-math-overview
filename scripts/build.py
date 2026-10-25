#!/usr/bin/env python3
"""Validate curated metadata and render the project and reading indexes."""
import argparse
import datetime
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'foundation': 'Mathematical foundations',
    'literature': 'Literature and document processing',
    'proving': 'Formal theorem proving',
    'reasoning': 'Mathematical reasoning',
    'discovery': 'Mathematical and algorithmic discovery',
    'verification': 'Informal verification',
    'attribution': 'Contribution attribution',
    'evaluation': '评测基准与研究材料',
}


def load():
    repos = json.loads((ROOT / 'data/repositories.json').read_text())
    readings = json.loads((ROOT / 'data/readings.json').read_text())
    for rows, fields in [
        (repos, {'id', 'name', 'url', 'category', 'description_zh', 'availability',
                 'source_role', 'checked_on', 'license', 'archived', 'role',
                 'selection_reason_zh', 'limitation_zh', 'tier'}),
        (readings, {'id', 'title', 'url', 'category', 'date', 'kind', 'note_zh',
                    'repository', 'checked_on', 'reading_scope'}),
    ]:
        ids, urls = set(), set()
        for row in rows:
            assert fields <= row.keys(), f'Missing fields: {row.get("id")}'
            assert row['id'].lower() not in ids, f'Duplicate ID: {row["id"]}'
            assert row['url'].lower() not in urls, f'Duplicate URL: {row["url"]}'
            ids.add(row['id'].lower())
            urls.add(row['url'].lower())
            assert row['category'] in CATEGORIES, row['category']
            parsed = urlparse(row['url'])
            assert parsed.scheme == 'https' and parsed.netloc, row['url']
            datetime.date.fromisoformat(row['checked_on'])
    ids = {r['id'] for r in repos}
    for r in repos:
        assert r['url'] == 'https://github.com/' + r['id']
        assert r['source_role'] in {'upstream', 'third-party'}
        assert r['tier'] in {'representative', 'focused-case'}
        assert isinstance(r['archived'], bool)
    for p in readings:
        assert p['repository'] is None or p['repository'] in ids, p['repository']
        assert p['kind'] in {'paper', 'article'}
        assert datetime.date.fromisoformat(p['date']) <= datetime.date.fromisoformat(p['checked_on'])
    return repos, readings


def cell(text):
    return str(text).replace('|', '\\|').replace('\n', ' ')


def render(repos, readings):
    resources = '''# Selected Projects

[Overview](../README.md) · [Infrastructure](infrastructure.md) · [Selection criteria](methodology.md)

保留各层具有代表性和可复用性的项目。每个入口说明它解决的环节、收录理由和对贡献归因的边界。同一路线的历史版本不另起条目。

'''
    for category, title in CATEGORIES.items():
        group = [r for r in repos if r['category'] == category]
        if not group:
            continue
        resources += f'## {title}\n\n| 项目 | 角色与收录理由 | 能力边界 |\n| --- | --- | --- |\n'
        for r in group:
            label = '（专题案例）' if r['tier'] == 'focused-case' else ''
            resources += f'| [{cell(r["name"])}]({r["url"]}){label} | **{cell(r["role"])}**。{cell(r["selection_reason_zh"])} | {cell(r["limitation_zh"])} |\n'
        resources += '\n'
    doc = '''# Selected Readings

[Overview](../README.md) · [Contribution attribution](contribution-attribution.md) · [Research gaps](research-gaps.md)

## Research focus

- **局部验证**：[OSVerify §3](https://arxiv.org/html/2610.18089v1#S3)，理解分解、提议和验证的任务边界。
- **文献对应**：[math-lineage](https://github.com/jnshi/math-lineage)，查看证据位置、关系分类与实际报告。
- **新颖性信号**：PriorProof 与 Beyond Correctness，比较形式化依赖、检索与专家判断。
- **宏观归因**：Who Solved It?，仅依据公开摘要讨论聚合与文献依赖问题。

下列论文按技术路线组织。arXiv 日期为首次提交日期；原始实验条件与结果应以论文为准。新颖性相关预印本用于近邻工作比较，其成熟度与基础设施项目分开评估。

'''
    for category, title in CATEGORIES.items():
        group = [p for p in readings if p['category'] == category]
        if not group:
            continue
        doc += f'## {title}\n\n| 日期 | 文献 | 研究关联 |\n| --- | --- | --- |\n'
        for p in sorted(group, key=lambda p: p['date']):
            label = ' [官方文章]' if p['kind'] == 'article' else ''
            scope = ' **仅摘要。**' if p['reading_scope'] == 'abstract-only' else ''
            doc += f'| {p["date"]} | [{cell(p["title"])}]({p["url"]}){label} | {cell(p["note_zh"])}{scope} |\n'
        doc += '\n'
    bib = '% Discovery references. Obtain complete citation metadata from each primary source.\n\n'
    for p in readings:
        title = p['title'].replace('&', r'\&').replace('%', r'\%').replace('_', r'\_')
        key = 'aimath' + p['id'].replace('.', '').replace('-', '')
        bib += f'@misc{{{key},\n  title = {{{{{title}}}}},\n  year = {{{p["date"][:4]}}},\n  url = {{{p["url"]}}}\n}}\n\n'
    return {'docs/resources.md': resources.rstrip() + '\n', 'docs/readings.md': doc.rstrip() + '\n',
            'references.bib': bib.rstrip() + '\n'}


def check_local_links():
    import re
    for path in [ROOT / 'README.md', ROOT / 'CONTRIBUTING.md', *sorted((ROOT / 'docs').glob('*.md'))]:
        for url in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            parsed = urlparse(url)
            if parsed.scheme or url.startswith('#'):
                continue
            assert (path.parent / parsed.path).exists(), f'Broken local link: {path.name}: {url}'


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
    check_local_links()
    print(f'Validated {len(repos)} projects, {len(readings)} readings, generated indexes and local links.')


if __name__ == '__main__':
    main()
