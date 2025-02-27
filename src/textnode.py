from enum import Enum
from leaf_node import LeafNode

class TextType(Enum):
    Normal_text = "normal"
    Bold_text = "bold"
    Italic_text = "italic"
    Code_text = "code"
    Links = "link"
    Images = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (self.text, self.text_type, self.url) == (other.text, other.text_type, other.url)
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.Normal_text:
        return LeafNode(None, text_node.text)
        
    elif text_node.text_type == TextType.Bold_text:
        return LeafNode("b", text_node.text)
        
    elif text_node.text_type == TextType.Italic_text:
        return LeafNode("i", text_node.text)
        
    elif text_node.text_type == TextType.Code_text:
        return LeafNode("code", text_node.text)
        
    elif text_node.text_type == TextType.Links:
        props = {"href": text_node.url}
        return LeafNode("a", text_node.text, props)
        
    elif text_node.text_type == TextType.Images:
        props = {
            "src": text_node.url,
            "alt": text_node.text
        }
        return LeafNode("img", "", props)
        
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")
