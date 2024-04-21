import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    )


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        """
        Test the equality of two TextNode objects.

        This test case creates two TextNode objects with the same text and text type. It then asserts that the two
        objects are equal using the `assertEqual` method.

        Parameters:
            self (TestTextNode): The test case instance.

        Returns:
            None
        """
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        """
        Test the inequality of two TextNode objects.

        This test case creates two TextNode objects with different text types. It then asserts that the two objects
        are not equal using the `assertNotEqual` method.

        Parameters:
            self (TestTextNode): The test case instance.

        Returns:
            None
        """
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false3(self):
        """
        Test the inequality of two TextNode objects.

        This test case creates two TextNode objects with the same text types but different text (case). It then
        asserts that the two objects are not equal using the `assertNotEqual` method.

        Parameters:
            self (TestTextNode): The test case instance.

        Returns:
            None
        """
        node = TextNode("This is a text Node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        """
        Test the equality of two TextNode objects with a URL.

        This test case creates two TextNode objects with the same text, text type, and URL. It then asserts that the
        two objects are equal using the `assertEqual` method.

        Parameters:
            self (TestTextNode): The test case instance.

        Returns:
            None
        """
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode(
                "This is a text node", text_type_italic, "https://www.boot.dev"
                )
        self.assertEqual(node, node2)

    def test_repr(self):
        """
        Test the representation of a TextNode object with text, text type, and URL.

        This test case creates a TextNode object with text, text type, and URL and asserts that the representation
        matches the expected value.

        Parameters:
            self (TestTextNode): The test case instance.

        Returns:
            None
        """
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
                "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
                )

    def test_repr2(self):
        """
        Test the `__repr__` method of the `TextNode` class.

        This test case creates a TextNode object with text, text type and asserts that the representation matches the
        expected value.

        Parameters:
            self (TestCase): The test case instance.

        Returns:
            None
        """
        node = TextNode("This is a text node", text_type_text)
        self.assertEqual(
                "TextNode(This is a text node, text, None)", repr(node)
                )


if __name__ == "__main__":
    unittest.main()
