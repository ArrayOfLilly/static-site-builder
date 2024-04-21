import os.path as path

from os import mkdir
from markdown_block import markdown_to_html_node


def extract_title(markdown):
    """
    Extracts the title from the markdown content by converting it to an HTML node tree.

    Args:
        markdown (str): The markdown string to extract the title from.

    Returns:
        str: The extracted title from the markdown content.

    Raises:
        ValueError: If the markdown is empty or if there is no heading 1 found in the markdown.
    """
    if len(markdown) <= 0:
        raise ValueError("Invalid markdown: empty document")

    page = markdown_to_html_node(markdown)
    title = []

    for node in page.children:
        if node.tag == "h1":
            for child in node.children:
                title.append(child.value)

    if title == []:
        raise ValueError("Invalid markdown: missing heading 1")

    return "".join(title)


def generate_page(from_path, template_path, dest_path):
    """
    Generates a static HTML page from a Markdown file using a template.

    Args:
        from_path (str): The path to the input Markdown file.
        template_path (str): The path to the template HTML file.
        dest_path (str): The destination path to save the generated HTML file.

    Raises:
        ValueError: If the input file does not exist.

    Returns:
        None

    This function reads the content of the input Markdown file,
    generates HTML from it using the `markdown_to_html_node` function,
    extracts the title from the Markdown content, and
    replaces placeholders in the template HTML with the extracted title and generated HTML content.
    Finally, it writes the generated HTML to a file at the specified destination path,
    creating any necessary directories if they don't exist.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # generating html from markdown
    markdown = ""

    if path.exists(from_path) and path.isfile(from_path):
        with open(from_path, "r") as file:
            markdown = file.read()
    else:
        raise ValueError("Invalid input: file does not exists")

    node = markdown_to_html_node(markdown)
    content = node.to_html()
    title = extract_title(markdown)

    # generating new staic page from generated html and template
    with open(template_path, "w") as file:
        template = file.read()

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    # Write the new HTML to a file at dest_path
    if not path.exists(dest_path):
        mkdir(dest_path)
    with open(dest_path, "w") as file:
        file.wrtite(page)
