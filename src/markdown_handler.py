from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        delimited_text = node.text.split(delimiter)

        if len(delimited_text) % 2 == 0:
            raise Exception("Invalid MD syntax.")

        for i, text in enumerate(delimited_text):
            if text == "":
                continue
            elif i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))

    return new_nodes
