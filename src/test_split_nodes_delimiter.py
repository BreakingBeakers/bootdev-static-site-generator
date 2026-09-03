import unittest

from split_nodes_delimiter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_empty_str(self):
        node = TextNode("", TextType.TEXT)
        split = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(split, [])

    def test_bold_split(self):
        node = TextNode("You are starting to get **bold**", TextType.TEXT)
        split = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            split,
            [
                TextNode("You are starting to get ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
            ],
        )

    def test_italic_split(self):
        node = TextNode("You are starting to get _italic_", TextType.TEXT)
        split = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            split,
            [
                TextNode("You are starting to get ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
        )

    def test_code_split(self):
        node = TextNode("You are starting to get `code`", TextType.TEXT)
        split = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            split,
            [
                TextNode("You are starting to get ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ],
        )

    def test_empty_with_delimiter(self):
        node = TextNode("``", TextType.TEXT)
        split = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(split, [])

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://wikipedia.org"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
