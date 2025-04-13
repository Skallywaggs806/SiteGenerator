from enum import Enum


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
    
    