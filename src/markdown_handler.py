import re

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


def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        current_text = node.text

        for link in links:
            value = link[0]
            href = link[1]
            sections = current_text.split(f"[{value}]({href})", 1)

            if len(sections) != 2:
                raise ValueError("invalid MD syntax")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(value, TextType.LINK, href))

            current_text = sections[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        current_text = node.text

        for image in images:
            value = image[0]
            href = image[1]
            sections = current_text.split(f"![{value}]({href})", 1)

            if len(sections) != 2:
                raise ValueError("invalid MD syntax")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(value, TextType.IMAGE, href))

            current_text = sections[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def extract_markdown_images(text: str):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text: str):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
