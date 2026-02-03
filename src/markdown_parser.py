from leafnode import LeafNode
from markdown_block import BlockType, block_to_block_type, markdown_to_blocks
from markdown_inline import text_to_textnodes
from parentnode import ParentNode
from textnode import text_node_to_html_node


def paragraph_to_node(text):
    children = []
    text_nodes = text_to_textnodes(text)

    for text_node in text_nodes:
        text_node.text = text_node.text.replace("\n", " ")
        children.append(text_node_to_html_node(text_node))

    return ParentNode("p", children)


def heading_to_node(text):
    children = []
    heading_level = len(text) - len(text.lstrip("#"))

    text = text.lstrip("#").strip()
    text_nodes = text_to_textnodes(text)

    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return ParentNode(f"h{heading_level}", children)


def code_to_node(text):
    inner_text = "\n".join(text.split("\n")[1:-1])
    code_node = LeafNode("code", inner_text)

    return ParentNode("pre", [code_node])


def quote_to_node(text):
    children = []

    lines = text.split("\n")
    clean_lines = [line.lstrip("> ").strip() for line in lines if line.strip()]
    clean_text = " ".join(clean_lines)
    text_nodes = text_to_textnodes(clean_text)

    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return ParentNode("blockquote", children)


def unordered_list_to_node(text):
    children = []
    list_items = text.split("\n")

    for list_item in list_items:
        list_children = []
        list_item = list_item.lstrip("- ").strip()
        text_nodes = text_to_textnodes(list_item)

        for text_node in text_nodes:
            list_children.append(text_node_to_html_node(text_node))

        children.append(ParentNode("li", list_children))

    return ParentNode("ul", children)


def ordered_list_to_node(text):
    children = []
    list_items = text.split("\n")

    for list_item in list_items:
        list_children = []
        list_item = list_item.split(". ", 1)[1]
        text_nodes = text_to_textnodes(list_item)

        for text_node in text_nodes:
            list_children.append(text_node_to_html_node(text_node))

        children.append(ParentNode("li", list_children))

    return ParentNode("ol", children)


def text_to_children(text):
    block_type = block_to_block_type(text)

    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_node(text)
    elif block_type == BlockType.HEADING:
        return heading_to_node(text)
    elif block_type == BlockType.CODE:
        return code_to_node(text)
    elif block_type == BlockType.QUOTE:
        return quote_to_node(text)
    elif block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_node(text)
    elif block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_node(text)

    return None


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []

    for block in blocks:
        nodes.append(text_to_children(block))

    html_node = ParentNode("div", nodes)
    return html_node


if __name__ == "__main__":
    md = """
# Heading Here

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

```
This is text that _should_ remain
the **same** even with inline stuff
```

- this is
- unordered
- list

1. And this
2. is unordered
3. list with **some**
4. **formatting** here _too_

> This is a quote
> that spans multiple
> lines and has **bold** text
"""
    html_node = markdown_to_html_node(md)
    print(html_node)
