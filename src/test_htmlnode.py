import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        """
        Test the `props_to_html` method of the `HTMLNode` class.

        This test case creates an instance of the `HTMLNode` class with the following parameters:
        - Tag name: "div"
        - Content: "Hello, world!"
        - Children nodes: None
        - Properties: {"class": "greeting", "href": "https://boot.dev"}

        The `props_to_html` method is then called on the `node` object and the resulting HTML string is compared to the expected value:
        - Expected HTML string: ' class="greeting" href="https://boot.dev"'

        This test ensures that the `props_to_html` method correctly converts the properties of the HTML node to the corresponding HTML attributes.

        Returns:
            None
        """
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_to_html_no_children(self):
        """
        Test the `to_html` method of the `LeafNode` class when there are no children nodes.

        This test case creates an instance of the `LeafNode` class with the following parameters:
        - Tag name: "p"
        - Content: "Hello, world!"
        - Children nodes: None

        The `to_html` method is then called on the `node` object and the resulting HTML string is compared to the expected value:
        - Expected HTML string: "<p>Hello, world!</p>"

        This test ensures that the `to_html` method correctly converts the `LeafNode` object to the corresponding HTML string when there are no children nodes.

        Returns:
            None
        """
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        """
        Test the `to_html` method of the `LeafNode` class when the tag is `None`.

        This test case creates an instance of the `LeafNode` class with the following parameters:
        - Tag name: `None` (plain text)
        - Content: "Hello, world!"

        The `to_html` method is then called on the `node` object and the resulting HTML string is compared to the expected value:
        - Expected HTML string: "Hello, world!"

        This test ensures that the `to_html` method correctly returns the content of the HTML node when the tag is `None`.

        Returns:
            None
        """
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        """
        Test the `to_html` method of the `ParentNode` class when there are children nodes.

        This test case creates a `LeafNode` object with the tag name "span" and content "child".
        It then creates a `ParentNode` object with the tag name "div" and a list containing the child node, which is the created LeafNode.
        The `to_html` method is called on the `parent_node` object and the resulting HTML string is compared to the expected value:
        - Expected HTML string: "<div><span>child</span></div>"

        This test ensures that the `to_html` method correctly converts the `ParentNode` object to the corresponding HTML string when there are children nodes.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        """
        Test the `to_html` method of the `ParentNode` class when there are grandchildren nodes.

        This test case creates a `LeafNode` object with the tag name "b" and content "grandchild".
        It then creates a `ParentNode` object with the tag name "span" and a list containing the grandchild node.
        Finally, it creates a `ParentNode` object with the tag name "div" and a list containing the child node.

        The `to_html` method is called on the `parent_node` object and the resulting HTML string is compared to the expected value:
        - Expected HTML string: "<div><span><b>grandchild</b></span></div>"

        This test ensures that the `to_html` method correctly converts the `ParentNode` object to the corresponding HTML string when there are grandchildren nodes.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        """
        Test the `to_html` method of the `ParentNode` class when there are many children nodes.

        This test case creates a `ParentNode` object with the tag name "p" and a list of children nodes.
        The children nodes include `LeafNode` objects with different tag names and contents.
        The `to_html` method is called on the `node` object and the resulting HTML string is compared to the expected value.
        The expected HTML string is constructed by concatenating the HTML strings of the children nodes.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        """
        Test the `to_html` method of the `ParentNode` class when there are many children nodes.

        This test case creates a `ParentNode` object with the tag name "h2" and a list of children nodes.
        The children nodes include `LeafNode` objects with different tag names and contents.
        The `to_html` method is called on the `node` object and the resulting HTML string is compared to the expected value.
        The expected HTML string is constructed by concatenating the HTML strings of the children nodes.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
