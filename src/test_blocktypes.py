import unittest
from blocktypes import BlockType, block_to_blocktype

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_blocktype(self):
        # Test for heading
        self.assertEqual(block_to_blocktype("# Heading"), BlockType.HEADING)
        
        # Test for paragraph
        self.assertEqual(block_to_blocktype("This is a paragraph."), BlockType.PARAGRAPH)
        
        # Test for code block
        self.assertEqual(block_to_blocktype("```python\nprint('Hello, World!')\n```"), BlockType.CODE)
        
        # Test for quote
        self.assertEqual(block_to_blocktype("> This is a quote."), BlockType.QUOTE)
        
        # Test for unordered list
        self.assertEqual(block_to_blocktype("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)
        
        # Test for ordered list
        self.assertEqual(block_to_blocktype("1. First item\n2. Second item"), BlockType.ORDERED_LIST)


