from enum import Enum
from .htmlnode import HTMLNode, LeafNode, ParentNode


class TextType(Enum):
    """Enum for text types."""
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"



class TextNode:
    """Class for text nodes."""

    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__ (self, other):
        if isinstance(other, TextNode):
            return self.text == other.text and self.text_type == other.text_type
        return False

    def __repr__(self):
        return f"TextNode(text={self.text}, type={self.text_type}, url={self.url})"
    

def text_node_to_html_node(text_node):
    """Convert a TextNode to an HTMLNode."""
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value=" ", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")
    
    