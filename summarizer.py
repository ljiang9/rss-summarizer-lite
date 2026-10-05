"""rss-summarizer-lite — RSS 聚合 + 摘要。

解析 RSS/Atom XML（标准库 xml），提取条目并做抽取式摘要。
内置样例 feed 离线演示。零第三方依赖。
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET

SAMPLE_FEED = """<?xml version="1.0"?>
<rss version="2.0"><channel>
<title>示例科技日报</title>
<item>
  <title>新模型发布</title>
  <description>研究团队今日发布新的大模型。新模型在多项基准上取得领先。训练成本大幅下降。社区反响热烈。</description>
</item>
<item>
  <title>开源工具更新</title>
  <description>一款流行的命令行工具发布新版本。新版本修复了多个已知问题，并引入更快的启动速度。</description>
</item>
</channel></rss>"""


def parse_feed(xml_text: str) -> list[dict]:
    """解析 RSS/Atom，返回 [{title, summary}]。"""
    root = ET.fromstring(xml_text)
    items = []
    for node in root.iter():
        tag = node.tag.split("}")[-1]
        if tag in ("item", "entry"):
            title = ""
            desc = ""
            for child in node:
                ctag = child.tag.split("}")[-1]
                if ctag == "title":
                    title = (child.text or "").strip()
                elif ctag in ("description", "summary", "content"):
                    desc = (child.text or "").strip()
            items.append({"title": title, "summary": desc})
    return items


def summarize(text: str, max_sentences: int = 2) -> str:
    """抽取式摘要：按句切分，取词频最高词所在的前 N 句。"""
    sents = re.split(r"(?<=[。！？.!?])", text)
    sents = [s.strip() for s in sents if s.strip()]
    if len(sents) <= max_sentences:
        return text.strip()
    words = re.findall(r"[a-zA-Z]+|[\u4e00-\u9fff]", text.lower())
    from collections import Counter
    freq = Counter(words)
    scored = sorted(
        range(len(sents)),
        key=lambda i: sum(freq.get(w, 0) for w in re.findall(r"[a-zA-Z]+|[\u4e00-\u9fff]", sents[i].lower())),
        reverse=True,
    )
    picked = sorted(scored[:max_sentences])
    return "".join(sents[i] for i in picked)


def run(xml_text: str) -> list[dict]:
    items = parse_feed(xml_text)
    for it in items:
        it["headline_summary"] = summarize(it["summary"])
    return items
