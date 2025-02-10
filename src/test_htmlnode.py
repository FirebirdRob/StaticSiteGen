import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        # Test with no props (should return empty string)
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_one_prop(self):
        # Test with one prop
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        # Test with multiple props
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        # The order of props might vary, so we need to check for both possibilities
        result = node.props_to_html()
        possible_results = [
            ' href="https://www.google.com" target="_blank"',
            ' target="_blank" href="https://www.google.com"'
        ]
        self.assertIn(result, possible_results)

if __name__ == "__main__":
    unittest.main()