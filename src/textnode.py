from htmlnode import LeafNode

# inline text types
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


# represent one inline text node
# intermediate representation between Markdown and HTML
class TextNode:

    def __init__(self, text, text_type, url=None):
        """
        Initializes a new instance of the TextNode class.

        Parameters:
            text (str): The text content of the text node.
            text_type (str): The type of the text node.
            url (str): The URL associated with the text node. Defaults to None.
        """
        # text content of the node
        self.text = text
        # type of text this node contain
        self.text_type = text_type
        # URL of the link or image
        self.url = url

    def __eq__(self, other):
        """
        Check if this object is equal to another object.

        Parameters:
            other (object): The object to compare to.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        """
        Returns a string representation of the TextNode object.

        :return: A string representation of the TextNode object.
        :rtype: str
        """
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    """
    Convert a textnode to an HTMLnode.

    Args:
        text_node (TextNode): The text node to be converted.

    Returns:
        LeafNode or ParentNode: The converted HTML node.

    Raises:
        ValueError: If the text type of the text node is invalid.
    """
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    raise ValueError(f"Invalid text type: {text_node.text_type}")


