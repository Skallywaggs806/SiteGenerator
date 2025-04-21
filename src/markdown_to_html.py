from markdown_to_block import markdown_to_blocks
from blocktypes import block_to_blocktype, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType



def text_to_children(text):
    """Convert text with inline markdown to a list of HTMLNode objects."""
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    div_node = ParentNode("div", None)  # Create parent div
    children = []  # To store all block nodes
    
    for block in blocks:
        block_type = block_to_blocktype(block)
        if block_type == BlockType.HEADING:
            # Count the number of # at the beginning of the heading
            heading_level = 0
            for char in block:
                if char == '#':
                    heading_level += 1
                else:
                    break
            
            # Make sure the heading level is between 1 and 6
            heading_level = min(6, heading_level)
            
            # Remove the # characters and any leading/trailing whitespace
            content = block[heading_level:].strip()
            
            # Create the heading node
            heading_node = LeafNode(f"h{heading_level}", content)
            heading_node.children = text_to_children(content)
            children.append(heading_node)
        elif block_type == BlockType.PARAGRAPH:
            para_node = LeafNode("p", None)
            para_node.children = text_to_children(block)
            children.append(para_node)

        elif block_type == BlockType.CODE:
            # Code blocks are special - they don't parse inline markdown
            # Remove the ``` markers from the beginning and end
            lines = block.split("\n")
            if lines[0].strip() == "```" and lines[-1].strip() == "```":
                code_content = "\n".join(lines[1:-1])
            else:
                # Handle case where ``` might be on the same line as content
                code_content = "\n".join(lines)
                if code_content.startswith("```"):
                    code_content = code_content[3:]
                if code_content.endswith("```"):
                    code_content = code_content[:-3]
            
            # Create TextNode for code content
            code_text_node = TextNode(code_content, text_type=TextType.TEXT)
            code_html_node = text_node_to_html_node(code_text_node)
            
            # Create the code node and pre node structure
            pre_node = ParentNode("pre", None)
            code_node = LeafNode("code", None)
            code_node.children = [code_html_node]
            pre_node.children = [code_node]
            children.append(pre_node)
        elif block_type == BlockType.QUOTE:
            # Remove the '>' prefix from each line and join
            lines = block.split('\n')
            quote_content = ""
            for line in lines:
                if line.startswith('> '):
                    quote_content += line[2:] + "\n"
                else:
                    quote_content += line + "\n"
            quote_content = quote_content.strip()
            
            quote_node = ParentNode("blockquote", None)
            quote_node.children = text_to_children(quote_content)
            children.append(quote_node)
        elif block_type == BlockType.UNORDERED_LIST:
            ul_node = ParentNode("ul", None)
            list_items = []
            
            # Split the block by lines and process each line as a list item
            for line in block.split('\n'):
                line = line.strip()
                if line.startswith('* '):  # Assuming unordered list items start with "* "
                    item_content = line[2:].strip()  # Remove the "* " prefix
                    li_node = HTMLNode("li", None)
                    li_node.children = text_to_children(item_content)
                    list_items.append(li_node)
            
            ul_node.children = list_items
            children.append(ul_node)
            
        elif block_type == BlockType.ORDERED_LIST:
            ol_node = ParentNode("ol", None)
            list_items = []
            
            # Split the block by lines and process each line as a list item
            for line in block.split('\n'):
                line = line.strip()
                if line and line[0].isdigit():  # Check if it starts with a digit
                    # Find the first non-digit, non-dot character
                    i = 0
                    while i < len(line) and (line[i].isdigit() or line[i] == '.'):
                        i += 1
                    item_content = line[i:].strip()  # Get content after the number and dot
                    li_node = HTMLNode("li", None)
                    li_node.children = text_to_children(item_content)
                    list_items.append(li_node)
            
            ol_node.children = list_items
            children.append(ol_node)
        else:
            raise ValueError(f"Unknown block type: {block_type}")
    div_node.children = children  # Assign children to the parent div
    return div_node
        
    