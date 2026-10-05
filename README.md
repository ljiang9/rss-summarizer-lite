# rss-summarizer-lite

RSS 聚合 + 摘要小工具。标准库解析 RSS/Atom XML，提取条目并做抽取式摘要。内置样例 feed 离线演示，零第三方依赖。

## 功能

- 标准库 `xml.etree` 解析 RSS `<item>` / Atom `<entry>`；
- 抽取式摘要：按句打分取关键句；
- 内置样例 feed，无需联网。

## 快速开始

```bash
python3 cli.py            # 离线样例
python3 cli.py -f feed.xml
```

## 无 API Key 如何运行

本工具**完全不需要 API Key**，摘要为本地抽取式。

## 目录结构

```
rss-summarizer-lite/
├── summarizer.py  # feed 解析、抽取式摘要、样例
├── cli.py
├── tests/test_summarizer.py
├── README.md / LICENSE / .gitignore
```

## 测试

```bash
python3 -m unittest discover -s tests
```

## 许可证

[MIT](./LICENSE)
