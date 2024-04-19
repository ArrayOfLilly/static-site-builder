import re
from pprint import pprint

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image, 
    text_type_link
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits the given list of TextNodes based on a delimiter and text type.

    Args:
        old_nodes (List[TextNode]): The list of TextNodes to be split.
        delimiter (str): The delimiter used to split the text.
        text_type (str): The text type to be assigned to the split sections.

    Returns:
        List[TextNode]: The list of split TextNodes.

    Raises:
        ValueError: If the formatted section is not closed.

    Description:
        This function takes a list of TextNodes and splits them based on a delimiter and text type.
        It iterates over each TextNode in the list and checks if its text type is not equal to text_type_text.
        If it is not, the TextNode is appended to the new_nodes list as is.
        Otherwise, the text of the TextNode is split using the delimiter.
        If the number of sections obtained after splitting is even, a ValueError is raised indicating an invalid markdown.
        The split sections are then iterated over.
        If a section is empty, it is skipped.
        If the index of the section is even, a new TextNode is created with the section text and text_type_text, and appended to the split_nodes list.
        If the index of the section is odd, a new TextNode is created with the section text and the specified text type, and appended to the split_nodes list.
        Finally, the split_nodes list is extended to the new_nodes list.
        The function returns the new_nodes list, which contains the split TextNodes.

    Example:
        old_nodes = [TextNode("Hello, **world**!", text_type_text), TextNode("This is a **test**.", text_type_text)]
    """
    new_nodes = []
    
    for old_node in old_nodes:
        # not a text type TextNode, we don't handle here
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []

        sections = old_node.text.split(delimiter)
        
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
    
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    """
    Extracts markdown images from the given text.

    Args:
        text (str): The text containing markdown image references.

    Returns:
        List[Tuple[str, str]]: A list of tuples, each containing the image name (alt) and the image URL.
    """
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    

def extract_markdown_links(text):
    """
    Extracts markdown links from the input text.
    :param text: The input text containing markdown links.
    :return: A list of tuples containing the link text and link URLs.
    """
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    """
    Splits the given list of TextNodes into a new list of TextNodes based on markdown image references.

    Args:
        old_nodes (List[TextNode]): The list of TextNodes to be split.

    Returns:
        List[TextNode]: The new list of TextNodes, split based on markdown image references.

    Description:
        This function takes a list of TextNodes and splits them based on markdown image references.
        It iterates over each TextNode in the list and checks if its text type is not equal to text_type_text.
        If it is not, the TextNode is appended to the new_nodes list as is.
        Otherwise, the text of the TextNode is checked for markdown image references using the extract_markdown_images function.
        If there are matches, the first match is obtained.
        The TextNode is split into sections using the markdown image reference as the delimiter.
        If the first section is not empty, a new TextNode is created with the first section text and text_type_text, and appended to the split_nodes list.
        A new TextNode is created with the image name (alt) and image URL extracted from the markdown image reference, and appended to the split_nodes list.
        If the second section is not empty, the split_nodes_image function is called recursively with a new TextNode containing the second section text and text_type_text, and the resulting split TextNodes are appended to the split_nodes list.
        Finally, the split_nodes list is extended to the new_nodes list.
        The function returns the new_nodes list, which contains the split TextNodes.

    Example:
        old_nodes = [TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", text_type_text)]
        split_nodes_image(old_nodes)
        # Returns:
        # [
        #     TextNode("This is text with an ", text_type_text),
        #     TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
        # ]
    """
    
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
                
        matches = extract_markdown_images(old_node.text)
        if matches:
            match = matches[0]
                    
            split_nodes = []
            
            sections = old_node.text.split(f"![{match[0]}]({match[1]})", 1)
            
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], text_type_text))
            split_nodes.append(TextNode(f"{match[0]}", "image", match[1]))
            if sections[1] != "":
                split_nodes.extend(split_nodes_image([TextNode(sections[1], text_type_text)]))
            
            new_nodes.extend(split_nodes)
        else:
            new_nodes.append(old_node)
    
    return new_nodes



def split_nodes_link(old_nodes):
    """
    Splits the given list of TextNodes based on markdown link references.

    Args:
        old_nodes (List[TextNode]): The list of TextNodes to be split.

    Returns:
        List[TextNode]: The list of split TextNodes, with markdown link references replaced with TextNodes of type "link".

    Description:
        This function takes a list of TextNodes and splits them based on markdown link references.
        It iterates over each TextNode in the list and checks if its text type is not equal to text_type_text.
        If it is not, the TextNode is appended to the new_nodes list as is.
        Otherwise, the text of the TextNode is checked for markdown link references using the extract_markdown_links function.
        If there are matches, the first match is obtained.
        The TextNode is split into sections using the markdown link reference as the delimiter.
        If the first section is not empty, a new TextNode is created with the first section text and text_type_text, and appended to the split_nodes list.
        A new TextNode is created with the link name (text) and link URL extracted from the markdown link reference, and appended to the split_nodes list.
        If the second section is not empty, the split_nodes_link function is called recursively with a new TextNode containing the second section text and text_type_text, and the resulting split TextNodes are appended to the split_nodes list.
        Finally, the split_nodes list is extended to the new_nodes list.
        The function returns the new_nodes list, which contains the split TextNodes.

    Example:
        old_nodes = [TextNode("This is text with a [link](https://example.com).", text_type_text)]
        split_nodes_link(old_nodes)
        # Returns:
        # [
        #     TextNode("This is text with a ", text_type_text),
        #     TextNode("link", text_type_link, "https://example.com"),
        # ]
    """
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
                
        matches = extract_markdown_links(old_node.text)
        if matches:
            match = matches[0]
                    
            split_nodes = []
            
            sections = old_node.text.split(f"[{match[0]}]({match[1]})", 1)
            
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], text_type_text))
            split_nodes.append(TextNode(f"{match[0]}", "link", match[1]))
            if sections[1] != "":
                split_nodes.extend(split_nodes_link([TextNode(sections[1], text_type_text)]))
            
            new_nodes.extend(split_nodes)
        else:
            new_nodes.append(old_node)
    
    return new_nodes


