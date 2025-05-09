from textnode import TextNode, TextType
from split_nodes import split_nodes_link, split_nodes_image
from node_splitter import split_nodes_delimiter
from markdown_extractor import extract_markdown_images, extract_markdown_links
import unittest


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.Normal_text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.Bold_text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Normal_text),
                TextNode("bolded", TextType.Bold_text),
                TextNode(" word", TextType.Normal_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.Normal_text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.Bold_text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Normal_text),
                TextNode("bolded", TextType.Bold_text),
                TextNode(" word and ", TextType.Normal_text),
                TextNode("another", TextType.Bold_text),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.Normal_text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.Bold_text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Normal_text),
                TextNode("bolded word", TextType.Bold_text),
                TextNode(" and ", TextType.Normal_text),
                TextNode("another", TextType.Bold_text),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.Normal_text)
        new_nodes = split_nodes_delimiter([node], "_", TextType.Italic_text)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.Normal_text),
                TextNode("italic", TextType.Italic_text),
                TextNode(" word", TextType.Normal_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.Normal_text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.Code_text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Normal_text),
                TextNode("code block", TextType.Code_text),
                TextNode(" word", TextType.Normal_text),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.Normal_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.Normal_text),
                TextNode("image", TextType.Images, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.Normal_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.Images, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.Normal_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.Normal_text),
                TextNode("image", TextType.Images, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.Normal_text),
                TextNode(
                    "second image", TextType.Images, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.Normal_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.Normal_text),
                TextNode("link", TextType.Links, "https://boot.dev"),
                TextNode(" and ", TextType.Normal_text),
                TextNode("another link", TextType.Links, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.Normal_text),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
