"""rss-summarizer-lite 单元测试。运行：python3 -m unittest discover -s tests"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from summarizer import parse_feed, summarize, run, SAMPLE_FEED  # noqa: E402


class TestParse(unittest.TestCase):
    def test_items(self):
        items = parse_feed(SAMPLE_FEED)
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]["title"], "新模型发布")

    def test_summary_field(self):
        items = parse_feed(SAMPLE_FEED)
        self.assertIn("基准", items[0]["summary"])


class TestSummarize(unittest.TestCase):
    def test_shorter(self):
        text = "研究团队发布新模型。新模型在多项基准领先。训练成本大幅下降。社区反响热烈。"
        s = summarize(text, max_sentences=2)
        self.assertLessEqual(s.count("。"), 2)

    def test_short_kept(self):
        text = "只有一句。"
        self.assertEqual(summarize(text), text)

    def test_run(self):
        items = run(SAMPLE_FEED)
        self.assertTrue(items[0]["headline_summary"])


if __name__ == "__main__":
    unittest.main()
