import markdown_extractor as ext
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    for node in old_nodes:
        images = ext.extract_markdown_images(node.text)



def split_nodes_link(old_node):
    pass