from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Props: {self.props}"
