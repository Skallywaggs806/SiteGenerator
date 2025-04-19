from enum import Enum

class BlockType(Enum):
    """
    Enum class representing different types of blocks.
    """
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_blocktype(block):
    """
    Convert a block to its corresponding BlockType.
    
    Args:
        block (str): The block to convert.
        
    Returns:
        BlockType: The corresponding BlockType.
    """
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("```"):
        return BlockType.CODE
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif block[0].isdigit() and block[1] == ".":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
