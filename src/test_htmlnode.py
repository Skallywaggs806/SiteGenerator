import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div", None, {"class": "container"})
        node2 = HTMLNode("div", "This is a div", None, {"class": "container"})
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("div", "This is a div", None, {"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=This is a div, children=None, props={'class': 'container'})")

    def test_eq_different_tag(self):
        node = HTMLNode("div", "This is a div", None, {"class": "container"})
        node2 = HTMLNode("span", "This is a div", None, {"class": "container"})
        self.assertNotEqual(node, node2)