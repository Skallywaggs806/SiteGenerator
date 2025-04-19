from markdown_to_block import markdown_to_blocks
from blocktypes import block_to_blocktype, BlockType
from htmlnode import HTMLNode


def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    div_node = HTMLNode("div", None)  # Create parent div
    children = []  # To store all block nodes
    
    for block in blocks:
        block_type = block_to_blocktype(block)
        if block_type == BlockType.HEADING:
            children.append(HTMLNode("h1", block))
        elif block_type == BlockType.PARAGRAPH:
            children.append(HTMLNode("p", block))
        elif block_type == BlockType.CODE:
            children.append(HTMLNode("pre", block))
        elif block_type == BlockType.QUOTE:
            children.append(HTMLNode("blockquote", block))
        elif block_type == BlockType.UNORDERED_LIST:
            children.append(HTMLNode("ul", block))
        elif block_type == BlockType.ORDERED_LIST:
            children.append(HTMLNode("ol", block))
        else:
            raise ValueError(f"Unknown block type: {block_type}")
    div_node.children = children  # Assign children to the parent div
    return div_node
        
    