from enum import Enum
import re
import markdown_extractor

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.heading
    if re.match(r"^```.*$```", block, re.DOTALL):
        return BlockType.code
    lines = block.split('\n')
    if lines and all(line.startswith(">") for line in lines):
        return BlockType.quote
    if lines and all(line.startswith("- ") for line in lines):
        return BlockType.unordered_list
    is_ordered_list = True
    for i, line in enumerate(lines, 1):
        if not line.startswith(f"{i}. "):
            is_ordered_list = False
            break
    if is_ordered_list == True:
        return BlockType.ordered_list
    
    else:
        return BlockType.paragraph