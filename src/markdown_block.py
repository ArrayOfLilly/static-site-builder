from textnode import text_node_to_html_node
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes

block_type_heading = "heading"
block_type_paragraph = "paragraph"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"
block_type_code = "code block"
block_type_quote = "quote"



def markdown_to_blocks(markdown):
    """
    Splits a given markdown string into blocks and returns a list of blocks.

    Args:
        markdown (str): The markdown string to be split into blocks.

    Returns:
        list: A list of blocks, where each block is a string representing a section of the markdown string.
    """
    raw_blocks = markdown.split("\n\n")
    blocks = []
    
    for block in raw_blocks:
        if block != "":
            blocks.append(block.strip())
    return blocks


def block_to_block_type(block):
    """
    Determines the type of a given block of markdown text.

    Args:
        block (str): The block of markdown text to be analyzed.

    Returns:
        str: The type of the block. Possible values are "heading", "unordered list", "ordered list", "code block",
        "quote", or "paragraph".

    Raises:
        ValueError: If the block is a code block but does not have the required closing symbols.

    """
    lines = block.split("\n")        
    
    # headings
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    
    # unordered list
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    
    # ordered list
    # if re.match(r"^\d+\.\s", block):
    #    for line in lines:
    #        if not lre.match(r"^\d+\.\s", block):
    #            return block_type_paragraph
    #    return block_type_ordered_list 
    
    # ordered list
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    
    # code block
    if len(lines) > 1 and block.startswith("```"):
        if block.endswith("```"):
            return block_type_code
        else:
            raise ValueError("Invalid block type: missing closings symbols")
    # quote block
    if block.startswith(">"):
        return block_type_quote
    
    # apragraph
    return block_type_paragraph
    

def text_to_children(text):
    """
    Convert a given text into a list of HTML nodes.
    
    Args:
        text (str): The input text to be converted.
        
    Returns:
        list: A list of HTML nodes representing the converted text.
    """
    text_nodes = text_to_textnodes(text)
    children = []
    
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def heading_to_html_node(block):
    """
    Convert a markdown heading block to an HTML heading node.

    Args:
        block (str): The markdown heading block to be converted.

    Returns:
        ParentNode: The converted HTML heading node.

    Raises:
        ValueError: If the heading level is invalid.

    This function takes a markdown heading block as input and converts it into an HTML heading node. It determines the
    level of the heading by counting the number of "#" characters at the beginning of the block. It then extracts the
    text of the heading and converts it into a list of HTML nodes using the `text_to_children` function. Finally, it
    creates an HTML heading node with the appropriate level and returns it.

    If the heading level is invalid (i.e., less than 1 or greater than 6), a ValueError is raised.

    Example:
        >> heading_to_html("# Heading 1")
        ParentNode("h1", [LeafNode(None, "Heading 1")])
    """
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def paragraph_to_html_node(block):
    """
    Convert a paragraph block to an HTML paragraph node.

    Args:
        block (str): The paragraph block to be converted.

    Returns:
        ParentNode: The converted HTML paragraph node.

    This function takes a paragraph block as input and converts it into an HTML paragraph node. It splits the block into
    lines, joins them into a single string, and then converts the string into a list of HTML nodes using the
    `text_to_children` function. Finally, it creates an HTML paragraph node with the children and returns it.

    Example:
        >> paragraph_to_html("This is a paragraph.\nIt has multiple lines.")
        ParentNode("p", [LeafNode(None, "This is a paragraph. It has multiple lines.")])
    """
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def unordered_list_to_html_node(block):
    """
    Convert an unordered list block to an HTML unordered list node.

    Args:
        block (str): The unordered list block to be converted.

    Returns:
        ParentNode: The converted HTML unordered list node.

    This function takes an unordered list block as input and converts it into an HTML unordered list node. It splits the
    block into individual list items, extracts the text from each item, and converts it into a list of HTML nodes using
    the `text_to_children` function. It then creates an HTML list item node for each item and appends them to the
    `html_items` list. Finally, it creates an HTML unordered list node with the `html_items` list as children and
    returns it.

    Example:
        >> unordered_list_to_html("- Item 1\n- Item 2\n- Item 3")
        ParentNode("ul", [ParentNode("li", [LeafNode(None, "Item 1")]), ParentNode("li", [LeafNode(None, "Item 2")]), ParentNode("li", [LeafNode(None, "Item 3")])])
    """
    list_items = block.split("\n")
    html_items = []
    for item in list_items:
        text = item[2:]
        children = text_to_children(text)
        html_item = ParentNode("li", children)
        html_items.append(html_item)
    return ParentNode("ul", html_items)


def ordered_list_to_html_node(block):
    """
    Convert an ordered list block to an HTML ordered list node.

    Args:
        block (str): The ordered list block to be converted.

    Returns:
        ParentNode: The converted HTML ordered list node.

    This function takes an ordered list block as input and converts it into an HTML ordered list node. It splits the
    block into individual list items, extracts the text from each item, and converts it into a list of HTML nodes using
    the `text_to_children` function. It then creates an HTML list item node for each item and appends them to the
    `html_items` list. Finally, it creates an HTML ordered list node with the `html_items` list as children and
    returns it.

    Example:
        >> ordered_list_to_html("1. Item 1\n2. Item 2\n3. Item 3")
        ParentNode("ol", [ParentNode("li", [LeafNode(None, "Item 1")]), ParentNode("li", [LeafNode(None, "Item 2")]), ParentNode("li", [LeafNode(None, "Item 3")])])
    """
    list_items = block.split("\n")
    html_items = []
    for item in list_items:
        for i in range(len(item)):
            if item[i] == ".":
                text = item[i + 2:]
                children = text_to_children(text)
                html_item = ParentNode("li", children)
                html_items.append(html_item)
    return ParentNode("ol", html_items)


def code_to_html_node(block):
    """
    Convert a markdown code block to an HTML code block.

    Args:
        block (str): The markdown code block to be converted.

    Returns:
        ParentNode: The converted HTML code block.

    Raises:
        ValueError: If the code block is invalid (does not start with "```" or does not end with "```").

    This function takes a markdown code block as input and converts it into an HTML code block. It checks if the code block
    starts with "```" and ends with "```". If not, it raises a ValueError. It then extracts the code text from the block
    and converts it into a list of HTML nodes using the `text_to_children` function. Finally, it creates an HTML code block
    node with the children and returns it.

    Example:
        >> code_to_html("```python\nprint("Hello, world!")\n```")
        ParentNode("pre", ParentNode("code", [LeafNode(None, "print(\"Hello, world!\")")]))
    """
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    return ParentNode("pre", ParentNode("code", children))


def quote_to_html_node(block):
    """
    Convert a quote block to an HTML blockquote element.

    Args:
        block (str): The quote block to be converted.

    Returns:
        ParentNode: The converted HTML blockquote element.

    Raises:
        ValueError: If the quote block is invalid (does not start with ">").

    This function takes a quote block as input and converts it into an HTML blockquote element. It splits the block into
    lines and iterates over each line. If a line does not start with ">", it raises a ValueError. It then removes the
    leading ">" character and any leading/trailing whitespace from each line. The lines are then joined into a single
    string. The string is converted into a list of HTML nodes using the `text_to_children` function. Finally, an HTML
    blockquote element is created with the children and returned.

    Example:
        >> quote_to_html("> This is a quote\n> With multiple lines")
        ParentNode("blockquote", [LeafNode(None, "This is a quote"), LeafNode(None, "With multiple lines")])
    """
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
        
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)


def block_to_html_node(block):
    """
    Convert a block of text to an HTML node based on its type.

    Args:
        block (str): The block of text to be converted.

    Returns:
        ParentNode: The converted HTML node based on the block type.

    Raises:
        ValueError: If the block type is invalid.

    This function takes a block of text as input and determines its type based on the `block_to_block_type` function. 
    It then converts the block to an HTML node based on its type using the appropriate conversion function. 
    The supported block types are:
    - Paragraph: `paragraph_to_html_node`
    - Heading: `heading_to_html_node`
    - Unordered List: `unordered_list_to_html_node`
    - Ordered List: `ordered_list_to_html_node`
    - Code: `code_to_html_node`
    - Quote: `quote_to_html_node`

    If the block type is not recognized, a `ValueError` is raised.

    Example:
        >> block_to_html_node("# Heading\nThis is a paragraph.")
        ParentNode("h1", [LeafNode(None, "Heading")])
    """
    block_type = block_to_block_type(block)
    
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    
    if block_type == block_type_unordered_list:
        return unordered_list_to_html_node(block)
    
    if block_type == block_type_ordered_list:
        return ordered_list_to_html_node(block)
    
    if block_type == block_type_code:
        return code_to_html_node(block)
    
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    
    raise ValueError("Invalid block type")


def markdown_to_html_node(markdown):
    """
    Convert a markdown string to an HTML node tree.

    Args:
        markdown (str): The markdown string to be converted.

    Returns:
        ParentNode: The root node of the HTML node tree.

    This function takes a markdown string as input and converts it into an HTML node tree. It first splits the markdown
    string into blocks using the `markdown_to_blocks` function. Then, it iterates over each block and converts it into an
    HTML node using the `block_to_html_node` function. The resulting HTML nodes are collected into a list called `children`.
    Finally, a `ParentNode` with the tag name "div" and the `children` list is returned, representing the root node of the
    HTML node tree.

    Example:
        >> markdown_to_html_node("# Heading\nThis is a paragraph.")
        ParentNode("div", [ParentNode("h1", [LeafNode(None, "Heading")]), ParentNode("p", [LeafNode(None, "This is a paragraph.")])])
    """
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        node = block_to_html_node(block)
        children.append(node)
    return ParentNode("div", children)




