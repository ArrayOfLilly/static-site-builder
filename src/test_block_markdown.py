import unittest

from block_markdown import markdown_to_blocks


# unit test class for testing the functionality of the block markdown
class TestBlockeMarkdown(unittest.TestCase):
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
        
        This test case verifies that the `markdown_to_blocks` function correctly trims the leading and trailing whitespace
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
                '# This is a heading', 
            ]
        )    
        
    def test_markdown_to_blocks_multiblock(self):
        """
        Test the `markdown_to_blocks` function with a markdown string that contains multiple blocks.
        
        This test case verifies that the `markdown_to_blocks` function correctly parses a markdown string with multiple blocks
        and returns a list of blocks. The markdown string contains a heading, a paragraph, a bolded paragraph, a paragraph with
        italic and code text, a list item, and another list item. The expected output is a list of blocks, where each block
        represents a section of the markdown string. The first block is the heading, the second block is the paragraph, the third
        block is the bolded paragraph, the fourth block is the paragraph with italic, code text, and a new line, and the fifth
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
                '# This is a heading', 
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                'This is **bolded** paragraph', 
                'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
                '* This is a list item\n* This is another list item'
            ]
        )

if __name__ == "__main__":
    unittest.main()
