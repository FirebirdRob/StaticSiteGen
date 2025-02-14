import unittest
from parent_node import ParentNode
from leaf_node import LeafNode

class TestParentNode(unittest.TestCase):
    def test_basic_parent_node(self):
        # Test a simple parent with one child
        node = ParentNode("div", [
            LeafNode("p", "Hello")
        ])
        self.assertEqual(node.to_html(), "<div><p>Hello</p></div>")
    
    def test_missing_tag(self):
        # Test that ValueError is raised when tag is None
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("p", "Hello")])
            node.to_html()

    def test_multiple_children(self):
        node = ParentNode("div", [
        LeafNode("b", "This will be bold"),      # A bold child
        LeafNode("i", "This will be italic"),    # An italic child
        LeafNode(None, "This is plain text"),    # A plain text child
        LeafNode("p", "This is a paragraph")     # A paragraph child
        ])
        expected = "<div><b>This will be bold</b><i>This will be italic</i>This is plain text<p>This is a paragraph</p></div>"
        self.assertEqual(node.to_html(), expected)

    def test_nested_parents(self):
        # Create an inner parent node
        inner_parent = ParentNode("div", [
            LeafNode("p", "This is inside the inner div")
        ])
        
        # Create the outer parent node that contains the inner parent
        outer_parent = ParentNode("div", [
            LeafNode("b", "This is bold"),
            inner_parent,  # Here's where we nest the parent!
            LeafNode("i", "This is italic")
        ])
        
        expected = "<div><b>This is bold</b><div><p>This is inside the inner div</p></div><i>This is italic</i></div>"
        self.assertEqual(outer_parent.to_html(), expected)

    def test_missing_children(self):
        # Test that ValueError is raised when children is None
        with self.assertRaises(ValueError):
            node = ParentNode("b", None)
            node.to_html()

if __name__ == '__main__':
    unittest.main()