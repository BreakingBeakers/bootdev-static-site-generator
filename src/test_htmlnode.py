import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_empty_html_node_has_no_props(self):
        node = HTMLNode()
        props = node.props_to_html()
        self.assertEqual(props, "")

    def test_eq(self):
        node = HTMLNode(props={"test": "test"})
        props = node.props_to_html()
        self.assertEqual(props, ' test="test"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Go Home", {"href": "localhost:8888"})
        self.assertEqual(node.to_html(), '<a href="localhost:8888">Go Home</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
