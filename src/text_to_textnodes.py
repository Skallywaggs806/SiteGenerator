
from .textnode import *
from .split_node import *
from .extract_markdown import *
from .inline_markdown import split_nodes_delimiter

def text_to_textnodes(text):
    """
    Convert a text string to a list of TextNode objects.
    """
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes

def main():
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    return text_to_textnodes(text)
if __name__ == "__main__":
    print(main())