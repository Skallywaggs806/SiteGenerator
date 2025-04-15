from enum import Enum

def markdown_to_blocks(markdown):

    blocks = []

    lines = markdown.split("\n\n")

    for line in lines:
        blocks.append(line.strip())
    
    return blocks
    



