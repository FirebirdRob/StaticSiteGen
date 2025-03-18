from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.Normal_text:
            while delimiter in node.text:
                open_pos = node.text.find(delimiter)
                close_pos = node.text.find(delimiter, open_pos + len(delimiter))

                if close_pos == -1:
                    raise ValueError(f"Unmatched delimiter '{delimiter}' in '{node.text}'")
                
                before = node.text[:open_pos]
                inside = node.text[open_pos + len(delimiter):close_pos]
                after = node.text[close_pos + len(delimiter):]

                if before:
                    new_nodes.append(TextNode(before, TextType.Normal_text))
                new_nodes.append(TextNode(inside, text_type))

                node.text = after

            if node.text:
                new_nodes.append(TextNode(node.text, TextType.Normal_text))

        else:
            new_nodes.append(node)

    return new_nodes