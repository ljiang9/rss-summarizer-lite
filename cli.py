"""命令行：python3 cli.py（离线样例）或 python3 cli.py -f feed.xml"""
import argparse
import json
import sys

from summarizer import run, SAMPLE_FEED


def main(argv=None):
    p = argparse.ArgumentParser(description="rss-summarizer-lite RSS 聚合+摘要")
    p.add_argument("-f", "--file", help="RSS/Atom XML 文件")
    p.add_argument("--sample", action="store_true", help="使用内置样例 feed")
    args = p.parse_args(argv)

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            xml_text = f.read()
    else:
        xml_text = SAMPLE_FEED
    print(json.dumps(run(xml_text), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
