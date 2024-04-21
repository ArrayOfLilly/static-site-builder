import unittest

from generate_static import extract_title


# unit test class for testing the functionality of the block markdown
class TestGenerateStatic(unittest.TestCase):
    

    def test_extract_title(self):
        """
        Test the extract_title function.

        This function tests the extract_title function by providing it with a sample markdown input containing a heading.
        It calls the extract_title function with the given markdown and asserts that the extracted title matches the expected title.

        Parameters:
            self (TestMarkdownToHTML): The instance of the TestMarkdownToHTML class.

        Returns:
            None
        """
        markdown = "1. apple\n2. pear\n\n# this is a *heading* with **strong** words\n\nthis is a paragraph.\n\n[Boot.dev](https://blog.boot.dev)"
        title = extract_title(markdown)
        self.assertEqual(
            title,
            "this is a heading with strong words"
            )
        
    # def test_extract_title_noheading(self):
    #     """
    #     Test the extract_title function when there is no heading in the markdown.

    #     This test case creates a markdown string without a heading.
    #     The extract_title function is called with the markdown string as input.
    #     The function is expected to raise a ValueError.

    #     Parameters:
    #         self (TestCase): The current test case instance.

    #     Returns:
    #         None
    #     """
    #     markdown = """
    #     1. apple
    #     2. pear
        
    #     this is not a *heading* with **strong** words
        
        
    #     this is a paragraph.
        
    #     [Boot.dev](https://blog.boot.dev)
        
    #     """
    #     title = extract_title(markdown)
    #     with self.assertRaises(ValueError):
    #         self.assertEqual(
    #             title,
    #             ""
    #         )
        
    # def test_extract_title(self):
    #     """
    #     Test the extract_title function.
        
    #     This function tests the extract_title function by providing it with an empty markdown input.
    #     It calls the extract_title function with the given markdown and asserts that the extracted title matches the expected title.

    #     Parameters:
    #         self (TestExtractTitle): The instance of the TestExtractTitle class.

    #     Returns:
    #         None
    #     """
    #     markdown = ""
    #     title = extract_title(markdown)
    #     with self.assertRaises(ValueError):
    #         self.assertEqual(
    #             title,
    #             ""
    #             )
        
if __name__ == "__main__":
    unittest.main()
