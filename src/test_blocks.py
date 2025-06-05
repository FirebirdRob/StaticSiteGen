from blocks import BlockType, block_to_block_type

def test_heading():
    block = "# This is a heading"
    expected_type = BlockType.heading
    assert block_to_block_type(block) == expected_type

def test_heading_level_6():
    block = "###### This is a level 6 heading"
    expected_type = BlockType.heading
    assert block_to_block_type(block) == expected_type

def test_code_block():
    block = "```\nprint('Hello, world!')\nx = 1 + 1\n```"
    expected_type = BlockType.code
    assert block_to_block_type(block) == expected_type

def test_quote_block():
    block = "> This is a quote.\n> It has multiple lines."
    expected_type = BlockType.quote
    assert block_to_block_type(block) == expected_type

def test_unordered_list():
    block = "- Item 1\n- Item 2\n- Item 3"
    expected_type = BlockType.unordered_list
    assert block_to_block_type(block) == expected_type

def test_unordered_list():
    block = "- Item 1\n- Item 2\n- Item 3"
    expected_type = BlockType.unordered_list
    assert block_to_block_type(block) == expected_type

def test_ordered_list():
    block = "1. First item\n2. Second item\n3. Third item"
    expected_type = BlockType.ordered_list
    assert block_to_block_type(block) == expected_type

def test_paragraph():
    block = "This is a normal paragraph of text.\nIt can have multiple lines."
    expected_type = BlockType.paragraph
    assert block_to_block_type(block) == expected_type

def test_heading_too_many_hashes_is_paragraph():
    block = "####### This is not a valid heading"
    # Based on the rules, if it doesn't fit the heading pattern (1-6 hashes followed by a space),
    # and it doesn't fit any other special types, it should be a paragraph.
    expected_type = BlockType.paragraph
    assert block_to_block_type(block) == expected_type

def test_heading_no_space_is_paragraph():
    block = "#NoSpaceHere"
    # Again, if it doesn't match the strict heading rule, it should fall through
    # and likely be classified as a paragraph.
    expected_type = BlockType.paragraph
    assert block_to_block_type(block) == expected_type

def test_incomplete_code_block_is_paragraph():
    block = "```\nThis block is missing the closing backticks"
    # If the code block pattern isn't fully matched (start AND end backticks),
    # it won't be a code block.
    expected_type = BlockType.paragraph
    assert block_to_block_type(block) == expected_type

def test_code_block_on_single_line_is_paragraph():
    block = "```print('This is code')```"
    # The instructions for code blocks imply the backticks should typically be on their own lines,
    # though the regex might need to be precise here based on your implementation.
    # Assuming a strict implementation where they need to be on separate lines, this would not match.
    expected_type = BlockType.paragraph # Or potentially BlockType.code if your regex allows it
    assert block_to_block_type(block) == expected_type

def test_partial_quote_is_paragraph():
    block = "> This is a quote line\nThis is not a quote line"
    # The rule for quotes is that *every* line must start with '>'.
    # If even one line doesn't, it's not a quote block.
    expected_type = BlockType.paragraph
    assert block_to_block_type(block) == expected_type

def test_unordered_list_no_space_is_paragraph():
    block = "-NoSpace"
    # Unordered lists require a space after the hyphen. Without it, it's just
    # a line starting with a hyphen, and thus not an unordered list block.
    expected_type = BlockType.paragraph
    assert block_to_block_type(block) == expected_type

def test_ordered_list_skipped_number_is_paragraph():
    block = "1. First item\n3. Third item"
    # Ordered lists must have sequentially increasing numbers starting from 1.
    # If a number is skipped, it doesn't fit the ordered list pattern.
    expected_type = BlockType.paragraph
    assert block_to_block_type(block) == expected_type

def test_ordered_list_starts_at_zero_is_paragraph():
    block = "0. First item\n1. Second item"
    # Ordered lists must start with 1. Starting with 0 means it doesn't fit
    # the ordered list pattern.
    expected_type = BlockType.paragraph
    assert block_to_block_type(block) == expected_type

def test_empty_block_is_paragraph():
    block = ""
    # An empty block doesn't fit any of the specific block types.
    expected_type = BlockType.paragraph
    assert block_to_block_type(block) == expected_type