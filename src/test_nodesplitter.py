from textnode import TextNode, TextType
from node_splitter import split_nodes_delimiter



def test_split_simple():
    node = TextNode("This is **bold** text", TextType.Normal_text)
    result = split_nodes_delimiter([node], "**", TextType.Bold)

    assert len(result) == 3
    assert result[0].text == "This is "
    assert result[0].text_type == TextType.Normal_text
    assert result[1].text == "bold"
    assert result[1].text_type == TextType.Bold
    assert result[2].text == " text"
    assert result[2].text_type == TextType.Normal_text

def test_unmatched_delimiter():
    try:
        node = TextNode("This is **bold text", TextType.Normal_text)
        split_nodes_delimiter([node], "**", TextType.Bold)
    except ValueError as e:
        assert str(e) == "Unmatched delimiter '**' in 'This is **bold text'"

def test_multiple_delimiters():
    node = TextNode("**first** and **second**", TextType.Normal_text)
    result = split_nodes_delimiter([node], "**", TextType.Bold)

    assert len(result) == 5
    assert result[0].text == ""
    assert result[0].text_type == TextType.Normal_text
    assert result[1].text == "first"
    assert result[1].text_type == TextType.Bold
    assert result[2].text == " and "
    assert result[2].text_type == TextType.Normal_text
    assert result[3].text == "second"
    assert result[3].text_type == TextType.Bold
    assert result[4].text == ""
    assert result[4].text_type == TextType.Normal_text

def test_no_delimiters():
    node = TextNode("This text has no bold", TextType.Normal_text)
    result = split_nodes_delimiter([node], "**", TextType.Bold)

    assert len(result) == 1
    assert result[0].text == "This text has no bold"
    assert result[0].text_type == TextType.Normal_text

def test_empty_string():
    node = TextNode("", TextType.Normal_text)
    result = split_nodes_delimiter([node], "**", TextType.Bold)

    assert len(result) == 1
    assert result[0].text == ""
    assert result[0].text_type == TextType.Normal_text

def run_tests():
    test_split_simple()
    test_unmatched_delimiter()
    test_multiple_delimiters()
    test_no_delimiters()
    test_empty_string()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()