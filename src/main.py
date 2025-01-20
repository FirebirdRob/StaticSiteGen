from textnode import TextNode, TextType

def main():
    node = TextNode("This is a text node", TextType.Bold_text, "https://www.example.com")
    print(node)

if __name__ == "__main__":
    main()