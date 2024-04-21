import unittest

from markdown_block import (
    block_type_paragraph,
    block_type_code,
    block_type_heading,
    block_type_ordered_list,
    block_type_quote,
    block_type_unordered_list,
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    )


# unit test class for testing the functionality of the block markdown
class TestMarkdownToBlock(unittest.TestCase):

    def test_markdown_to_blocks_empty(self):
        """
        Test the `markdown_to_blocks` function with an empty markdown string.

        This test case verifies that the `markdown_to_blocks` function correctly
        handles an empty markdown string and returns an empty list.

        Parameters:
            self (TestBlockMarkdown): The current test case instance.

        Returns:
            None
        """
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
                blocks,
                []
                )

    def test_markdown_to_blocks_trimblock(self):
        """
        Test the `markdown_to_blocks` function with a markdown string that has leading and trailing whitespace.

        This test case verifies that the `markdown_to_blocks` function correctly trims the leading and trailing
        whitespace
        from the markdown string and returns a list with a single block containing the trimmed heading.

        Parameters:
            self (TestBlockMarkdown): The current test case instance.

        Returns:
            None
        """
        markdown = "         # This is a heading          "
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
                blocks,
                [
                        "# This is a heading",
                        ]
                )

    def test_markdown_to_blocks_multiblock(self):
        """
        Test the `markdown_to_blocks` function with a markdown string that contains multiple blocks.

        This test case verifies that the `markdown_to_blocks` function correctly parses a markdown string with
        multiple blocks
        and returns a list of blocks. The markdown string contains a heading, a paragraph, a bolded paragraph,
        a paragraph with
        italic and code text, a list item, and another list item. The expected output is a list of blocks,
        where each block
        represents a section of the markdown string. The first block is the heading, the second block is the
        paragraph, the third
        block is the bolded paragraph, the fourth block is the paragraph with italic, code text, and a new line,
        and the fifth
        block is the list item.

        Parameters:
            self (TestMarkdownToBlocks): The current test case instance.

        Returns:
            None
        """
        markdown = """
# This is a heading



        This is a paragraph of text. It has some **bold** and *italic* words inside of it. 


    This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list item
* This is another list item
"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
                blocks,
                [
                        "# This is a heading",
                        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                        "This is **bolded** paragraph",
                        "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on "
                        "a new line",
                        "* This is a list item\n* This is another list item"
                        ]
                )

    def test_block_to_block_type_paragraph(self):
        """
        Test the function block_to_block_type with a paragraph block.

        This test case checks if the function block_to_block_type correctly identifies a paragraph block.
        It creates a sample paragraph block with some bold and italic words inside. Then, it calls the
        block_to_block_type function with the block as input. Finally, it asserts that the returned
        block type is equal to the block_type_paragraph constant.

        This test case is part of the test suite for the block_to_block_type function.

        Parameters:
        - self: The test case instance.

        Returns:
        - None
        """
        block = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_block_to_block_type_h1(self):
        """
        Test the function `block_to_block_type` with a heading block of level 1.

        This test case verifies that the `block_to_block_type` function correctly
        identifies a heading block of level 1 and returns the corresponding block type.

        Parameters:
            self (TestBlockMarkdown): The current test case instance.

        Returns:
            None
        """
        block = "# This is a heading 1"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_heading)

    def test_block_to_block_type_h2(self):
        """
        Test the function `block_to_block_type` with a heading block of level 2.

        This test case verifies that the `block_to_block_type` function correctly
        identifies a heading block of level 2 and returns the corresponding block type.

        Parameters:
            self (TestBlockMarkdown): The current test case instance.

        Returns:
            None
        """
        block = "## This is a heading 2"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_heading)

    def test_block_to_block_type_unordered_list(self):
        """
        Test the function `block_to_block_type` with a block representing an unordered list.

        This test case verifies that the `block_to_block_type` function correctly
        identifies a block representing an unordered list and returns the corresponding block type.

        Parameters:
            self (TestBlockMarkdown): The current test case instance.

        Returns:
            None
        """
        block = "* This is a listitem\n* This is another listitem\n* This is another listitem lastly"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_unordered_list)

    def test_block_to_block_type_non_unordered_list(self):
        """
        Test the function `block_to_block_type` with a block that is not an unordered list.

        This test case verifies that the `block_to_block_type` function correctly
        identifies a block that is not an unordered list and returns the corresponding block type.

        Parameters:
            self (TestBlockMarkdown): The current test case instance.

        Returns:
            None
        """
        block = "*This* is not a listitem\n*"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_block_to_block_type_ordered_list(self):
        """
        Test the function `block_to_block_type` with a block representing an ordered list.

        This test case verifies that the `block_to_block_type` function correctly
        identifies a block representing an ordered list and returns the corresponding block type.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        block = ("1. This is a numbered listitem\n2. This is another numbered listitem\n3. This is the last numbered "
                 "listitem")
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_ordered_list)

    def test_block_to_block_type_non_ordered_list(self):
        """
        Test the function `block_to_block_type` with a block that is not an ordered list.

        This test case verifies that the `block_to_block_type` function correctly
        identifies a block that is not an ordered list and returns the corresponding block type.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        block = "1 pieces non list item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_block_to_block_type_non_code(self):
        """
        Test the function `block_to_block_type` with a block that is not a code block.

        This test case verifies that the `block_to_block_type` function correctly
        identifies a block that is not a code block and returns the corresponding block type.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        block = "``````"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_paragraph)

    def test_block_to_block_type_code(self):
        """
        Test the function `block_to_block_type` with a code block.

        This test case verifies that the `block_to_block_type` function correctly
        identifies a code block and returns the corresponding block type.

        Parameters:
            self (TestBlockMarkdown): The current test case instance.

        Returns:
            None
        """
        block = "```\na\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_code)

    def test_block_to_block_type_quote(self):
        """
        Test the function `block_to_block_type` with a block representing a quote.

        This test case verifies that the `block_to_block_type` function correctly
        identifies a block representing a quote and returns the corresponding block type.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        block = "> apple"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_quote)


# External tests:
class TestMarkdownToHTML(unittest.TestCase):

    def test_markdown_to_blocks(self):
        """
        Test the markdown_to_blocks function.

        This function tests the markdown_to_blocks function by converting a given markdown string
        into blocks and comparing the result with the expected output.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                        "This is **bolded** paragraph",
                        "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on "
                        "a new line",
                        "* This is a list\n* with items",
                        ],
                )

    def test_markdown_to_blocks_newlines(self):
        """
        Test the `markdown_to_blocks` function with a markdown string that contains newlines.

        This test case verifies that the `markdown_to_blocks` function correctly parses a markdown string with
        newlines and returns a list of blocks. The markdown string contains a paragraph with bolded text, a paragraph
        with multiple newlines, a paragraph with italic and code text, and a list item. The expected output is a list
        of blocks, where each block represents a section of the markdown string. The first block is the bolded
        paragraph, the second block is the paragraph with multiple newlines and the same paragraph on a new line,
        and the third block is the list item.

        Parameters:
            self (TestMarkdownToBlocks): The current test case instance.

        Returns:
            None
        """
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                        "This is **bolded** paragraph",
                        "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on "
                        "a new line",
                        "* This is a list\n* with items",
                        ],
                )

    def test_block_to_block_types(self):
        """
        Test the conversion of a block of markdown to its corresponding block type.

        This function tests the `block_to_block_type` function by providing different
        blocks of markdown and checking if the returned block type matches the expected
        value. The function uses the `assertEqual` method from the `unittest.TestCase`
        class to compare the actual and expected block types.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None

        Raises:
            AssertionError: If the actual block type does not match the expected block type.
        """
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_paragraph(self):
        """
        Test the conversion of a Markdown paragraph to an HTML node.

        This function takes no parameters.

        It converts a Markdown paragraph to an HTML node using the `markdown_to_html_node` function.
        The Markdown paragraph is defined as follows:
        ```
        This is **bolded** paragraph
        text in a p
        tag here
        ```

        The resulting HTML node is then converted to HTML using the `to_html` method.
        The expected HTML output is:
        ```
        <div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>
        ```

        The function asserts that the generated HTML matches the expected HTML.

        This test ensures that the `markdown_to_html_node` function correctly converts Markdown paragraphs to HTML
        nodes.

        Returns:
            None
        """
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
                )

    def test_paragraphs(self):
        """
        Test the conversion of multiple paragraphs to HTML nodes.

        This function takes no parameters.

        It converts a Markdown paragraph with multiple lines into an HTML node using the `markdown_to_html_node`
        function.
        The Markdown paragraph is defined as follows:
        ```
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with *italic* text and `code` here
        ```

        The resulting HTML node is then converted to HTML using the `to_html` method.
        The expected HTML output is:
        ```
        <div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with
        <i>italic</i> text and <code>code</code> here</p></div>
        ```

        The function asserts that the generated HTML matches the expected HTML.

        This test ensures that the `markdown_to_html_node` function correctly converts multiple paragraphs to HTML
        nodes.

        Returns:
            None
        """
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with "
                "<i>italic</i> text and <code>code</code> here</p></div>",
                )

    def test_lists(self):
        """
        Test the conversion of Markdown lists to HTML nodes.

        This function takes no parameters.

        It converts a Markdown list to an HTML node using the `markdown_to_html_node` function.
        The Markdown list is defined as follows:
        ```
        - This is a list
        - with items
        - and *more* items

        1. This is an `ordered` list
        2. with items
        3. and more items
        ```

        The resulting HTML node is then converted to HTML using the `to_html` method.
        The expected HTML output is:
        ```
        <div>
          <ul>
            <li>This is a list</li>
            <li>with items</li>
            <li>and <i>more</i> items</li>
          </ul>
          <ol>
            <li>This is an <code>ordered</code> list</li>
            <li>with items</li>
            <li>and more items</li>
          </ol>
        </div>
        ```

        The function asserts that the generated HTML matches the expected HTML.

        This test ensures that the `markdown_to_html_node` function correctly converts Markdown lists to HTML nodes.

        Returns:
            None
        """
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This "
                "is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
                )

    def test_headings(self):
        """
        Test the conversion of Markdown headings to HTML.

        This function converts a Markdown string with headings (h1, h2, etc.) into an HTML string using the
        `markdown_to_html_node` function. It then compares the generated HTML string with the expected HTML string.

        Parameters:
            self (TestHeadings): The current test case instance.

        Returns:
            None

        Raises:
            AssertionError: If the generated HTML string does not match the expected HTML string.
        """
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
                )

    def test_blockquote(self):
        """
        Test the conversion of a Markdown blockquote to an HTML node.

        This function takes no parameters.

        It converts a Markdown blockquote to an HTML node using the `markdown_to_html_node` function.
        The Markdown blockquote is defined as follows:
        ```
        > This is a
        > blockquote block

        this is paragraph text
        ```

        The resulting HTML node is then converted to HTML using the `to_html` method.
        The expected HTML output is:
        ```
        <div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>
        ```

        The function asserts that the generated HTML matches the expected HTML.

        This test ensures that the `markdown_to_html_node` function correctly converts Markdown blockquotes to HTML
        nodes.

        Returns:
            None
        """
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
                )


if __name__ == "__main__":
    unittest.main()
