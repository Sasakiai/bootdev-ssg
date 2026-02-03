from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None
    ):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag cannot be empty")

        if not self.children:
            raise ValueError("Children cannot be empty")

        full = f"<{self.tag}{self.props_to_html()}>"

        for node in self.children:
            full += node.to_html()

        full += f"</{self.tag}>"

        return full

    def __repr__(self):
        return self.to_html()
