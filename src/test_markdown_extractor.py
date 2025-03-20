from markdown_extractor import extract_markdown_images, extract_markdown_links


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