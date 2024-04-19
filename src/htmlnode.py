# base class for creating HTML nodes
# defines the structure and behavior of an HTML node in a hierarchical manner
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initializes a new instance of the HTMLNode class.

        Parameters:
            tag (str): The tag of the HTML node. Defaults to None.
            value (str): The value of the HTML node. Defaults to None.
            children (list): The list of child nodes. Defaults to None.
            props (dict): The dictionary of properties. Defaults to None.
        """
        # string representing the HTML tag name
        self.tag = tag
        # string representing the value of the HTML tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        """
        Generates the HTML representation of the current object.

        :return: The HTML representation of the current object.
        :rtype: str
        :raises NotImplementedError: If the to_html method is not implemented.
        """
        raise NotImplementedError("to_html method not implememted")

    def props_to_html(self):
        """
        Generates the HTML representation of the attributes of the current object.

        :return: A string containing the HTML representation of the attributes of the current object as key, value pairs.
        :rtype: str
        """
        # if props contains values
        if self.props:
            attributes = ""
            
            for prop in self.props:
                attributes += f" {prop}=\"{self.props[prop]}\"" 
            return attributes

        # if props does not contains values
        return ""

    def __repr__(self):
        """
        Return a string representation of the HTMLNode object.

        :return: A string representation of the HTMLNode object.
        :rtype: str
        """
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


# subclass of HTMLNode, represents a single HTML element 
# it does not contain any other HTML elements
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        """
        Initializes a new instance of the LeafNode class.

        Parameters:
            tag (str): The tag of the HTML node.
            value (str): The value of the HTML node.
            props (dict, optional): The dictionary of properties. Defaults to None.
        """
        super().__init__(tag, value, None, props)

    def to_html(self):
        """
        Generates the HTML representation of the current object.

        :return: The HTML representation of the current object.
        :rtype: str
        :raises ValueError: If the HTML value is None and the tag is not None.
        """
        # can't be emmpty
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        # can be plain text
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        """
        Return a string representation of the LeafNode object.

        :return: A string representation of the LeafNode object.
        :rtype: str
        """
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


# subclass of HTMLNode, represents an HTML element 
# it contains other HTML elements, does not have own value
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        """
        Initializes a new instance of the ParentNode class.

        Parameters:
            tag (str): The tag of the HTML element.
            children (list): The list of child nodes.
            props (dict, optional): The dictionary of properties. Defaults to None.
        """
        super().__init__(tag, None, children, props)

    def to_html(self):
        """
        Generates the HTML representation of the current HTMLNode object and its children.

        Returns:
            str: The HTML representation of the current HTMLNode object and its children.

        Raises:
            ValueError: If the tag or children of the HTMLNode object are None.
        """
        # can't be plain text
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        # should have children
        if self.children is None:
            raise ValueError("Invalid HTML: no HTMLContent")
        
        inner_html = ""

        # recursively call it for all of it's children
        for child in self.children:
            inner_html += child.to_html()
        # opening tag with attributes, innerHTML (childrens), closing tag
        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"

    def __repr__(self):
        """
        Return a string representation of the ParentNode object.

        :return: A string representation of the ParentNode object.
        :rtype: str
        """
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
