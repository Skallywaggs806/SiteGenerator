import unittest

from extract_markdown import *

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is an image ![alt text](https://example.com/image.png)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("alt text", "https://example.com/image.png")])

    def test_extract_markdown_links(self):
        text = "This is a link [link text](https://example.com)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("link text", "https://example.com")])

