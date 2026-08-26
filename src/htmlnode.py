class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props = ""
        if self.props is not None:
            for key, value in self.props.items():
                props += f' {key}="{value}"'
        return props

    def __repr__(self) -> str:
        return f"HTMLNode{self.tag, self.value, self.children, self.props}"


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode{self.tag, self.value, self.props}"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list["HTMLNode"],
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode.to_html - Missing Tag")
        if self.children is None:
            raise ValueError("ParentNode.to_html - Missing Children")
        tree = f"<{self.tag}>"
        for child in self.children:
            tree += child.to_html()
        tree += f"</{self.tag}>"

        return tree
