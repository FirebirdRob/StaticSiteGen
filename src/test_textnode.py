import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold_text)
        node2 = TextNode("This is a text node", TextType.Bold_text)
        self.assertEqual(node, node2)

    def test_different_type(self):
        node = TextNode("This is a text node", TextType.Italic_text)
        node2 = TextNode("This is a text node", TextType.Code_text)
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.Normal_text)
        node2 = TextNode("This is a text node", TextType.Normal_text, "https://www.nodeexample.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()