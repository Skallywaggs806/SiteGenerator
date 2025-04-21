import unittest

from split_node import *
from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

from markdown_to_block import markdown_to_blocks
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html(self):
        markdown = "# Hello World\nThis is a paragraph.\n\n## Subheading\nThis is another paragraph.\n\n```python\nprint('Hello, world!')\n```"
        html_node = markdown_to_html_node(markdown)
        self.assertIsInstance(html_node, ParentNode)

    def test_code_markdown(self):
        markdown = "```python\nprint('Hello, world!')\n```"
        html_node = markdown_to_html_node(markdown)
        self.assertIsInstance(html_node, ParentNode)
    
    def test_heading_markdown(self):
        markdown = "# Heading 1\n## Heading 2\n### Heading 3"
        html_node = markdown_to_html_node(markdown)
        self.assertIsInstance(html_node, ParentNode)


    
    