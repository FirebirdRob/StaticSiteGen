from markdown_extractor import extract_markdown_images, extract_markdown_links, markdown_to_blocks


def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with a [link](https://www.example.com)"
    )
    self.assertListEqual([("link", "https://www.example.com")], matches)


def test_extract_markdown_nomatch_l(self):
    matches = extract_markdown_links(
        "This text has no links."
    )
    self.assertListEqual(matches, [])


def test_extract_markdown_nomatch_i(self):
    matches = extract_markdown_images(
        "This text has no images."
    )
    self.assertListEqual(matches, [])


def test_extract_multiple_markdown_i(self):
    matches = extract_markdown_images(
        "![image1](https://example1.com/image1.png) and ![image2](https://example2.com/image2.jpg)"
        )
    self.assertListEqual(matches, [("image1", "https://example1.com/image1.png"), ("image2", "https://example2.com/image2.jpg")])


def test_extract_multiple_markdown_l(self):
    matches = extract_markdown_links("[Google](https://google.com) and [GitHub](https://github.com)")
    self.assertListEqual(matches, [("Google", "https://google.com"), ("GitHub", "https://github.com")])


def test_extract_malformed_markdown_l(self):
    matches = extract_markdown_links("[malformed link](https://example")
    self.assertListEqual(matches, [])


def test_extract_malformed_markdown_i(self):
    matches = extract_markdown_images("![malformed image](https://example.com)")
    self.assertListEqual(matches, [])


def test_false_positives(self):
    matches = extract_markdown_links("Here is some text without any markdown links!")
    self.assertListEqual(matches, [])



def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

def test_empty(self):
    md = ""
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, [])

def test_excessive_newlines(self):
    md = """First paragraph


    Second paragraph


    

    Third paragraph"""

    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "First paragraph",
            "Second paragraph",
            "Third paragraph"
        ]
    )


def test_whitespace_handling(self):
    md = """   First paragraph with leading spaces   
    
  Second paragraph with different spacing\t\t
   
    Third paragraph after a line with only spaces    """
    
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "First paragraph with leading spaces",
            "Second paragraph with different spacing",
            "Third paragraph after a line with only spaces"
        ]
    )

def test_different_block_types(self):
    md = """# Heading 1

## Heading 2

Regular paragraph with **bold** and _italic_ text.

- List item 1
- List item 2

> This is a blockquote
> It can span multiple lines

```python
# This is a code block
def hello():
    print("Hello world")
```

---"""
    
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        len(blocks), 
        7,  # There should be 7 distinct blocks
    )
    self.assertTrue(blocks[0].startswith("# Heading 1"))
    self.assertTrue(blocks[1].startswith("## Heading 2"))
    self.assertTrue("**bold**" in blocks[2])
    self.assertTrue(blocks[3].startswith("- List"))
    self.assertTrue(blocks[4].startswith("> This"))
    self.assertTrue("```python" in blocks[5])
    self.assertTrue("---" in blocks[6] or "| Column" in blocks[6])