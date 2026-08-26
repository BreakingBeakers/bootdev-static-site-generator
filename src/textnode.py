from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: "TextType", url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value) -> bool:
        if isinstance(value, TextNode):
            return (
                self.text == value.text
                and self.text_type == value.text_type
                and self.url == value.url
            )
        return False

    def __repr__(self) -> str:
        return f"TextNode{self.text, self.text_type, self.url}"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode(
                "a",
                text_node.text,
                {"href": text_node.url if text_node.url is not None else ""},
            )
        case TextType.IMAGE:
            return LeafNode(
                "img",
                "",
                {
                    "src": text_node.url if text_node.url is not None else "",
                    "alt": text_node.text,
                },
            )
        case _:
            raise Exception("text_node_to_html_node: Unknown text type")
