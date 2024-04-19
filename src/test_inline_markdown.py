import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links, 
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

# unit test class for testing the functionality of the 
# split_nodes_delimiter, 
# extract_markdown_images, 
# extract_markdown_links, 
# split_nodes_image, and
# split_nodes_link functions
class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        """
        Test the split_nodes_delimiter function for the case of bold text delimiter.

        This function creates a TextNode object with the text "This is text with a **bolded** word" and the text_type_text.
        It then calls the split_nodes_delimiter function with the created TextNode object and the delimiter "**" and text_type_bold.
        The function asserts that the returned list of new_nodes matches the expected list of TextNode objects.

        Parameters:
        - self: The instance of the TestInlineMarkdown class.

        Returns:
        - None
        """
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        """
        Test the split_nodes_delimiter function for the case of bold text delimiter.

        This function creates a TextNode object with the text "This is text with a **bolded** word and **another**" and the text_type_text.
        More than one bold section in the text.
        It then calls the split_nodes_delimiter function with the created TextNode object and the delimiter "**" and text_type_bold.
        The function asserts that the returned list of new_nodes matches the expected list of TextNode objects.

        Parameters:
        - self: The instance of the TestInlineMarkdown class.

        Returns:
        - None
        """
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        """
        Test the split_nodes_delimiter function for the case of bold text delimiter with multiple words.

        This function creates a TextNode object with the text "This is text with a **bolded word** and **another**" and the text_type_text, 
        where one bold part is more than one word long.
        It then calls the split_nodes_delimiter function with the created TextNode object and the delimiter "**" and text_type_bold.
        The function asserts that the returned list of new_nodes matches the expected list of TextNode objects.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        """
        Test the split_nodes_delimiter function for the case of italic text delimiter.

        This function creates a TextNode object with the text "This is text with an *italic* word" and the text_type_text.
        It then calls the split_nodes_delimiter function with the created TextNode object and the delimiter "*" and text_type_italic.
        The function asserts that the returned list of new_nodes matches the expected list of TextNode objects.

        Parameters:
        - self: The instance of the TestInlineMarkdown class.

        Returns:
        - None
        """
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        """
        Test the split_nodes_delimiter function for the case of code delimiter.

        This function creates a TextNode object with the text "This is text with a `code block` word" and the text_type_text.
        It then calls the split_nodes_delimiter function with the created TextNode object and the delimiter "`" and text_type_code.
        The function asserts that the returned list of new_nodes matches the expected list of TextNode objects.

        Parameters:
        - self: The instance of the TestInlineMarkdown class.

        Returns:
        - None
        """
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_extract_image_noimage(self):
        """
        Test the extract_markdown_images function when there are no images in the text.

        This function creates a test case where the input text does not contain any images.
        It calls the extract_markdown_images function with the given text and asserts that
        the returned list of images is empty.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        text = "012[image1](linktoimage1)abc[](linktoimage2)xyz"
        images = extract_markdown_images(text)
        self.assertListEqual(
            images,
            []
        )

    def test_extract_image_image(self):
        """
        Test the extract_markdown_images function when there is one image in the text.

        This function creates a test case where the input text contains one image.
        It calls the extract_markdown_images function with the given text and asserts that
        the returned list of images matches the expected list.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        text = "012![image1](linktoimage1)abc"
        images = extract_markdown_images(text)
        self.assertListEqual(
            images,
            [
                ('image1', 'linktoimage1'), 
            ]
        )

    def test_extract_image_multiimage(self):
        """
        Test the extract_markdown_images function when there are multiple images in the text.

        This function creates a test case where the input text contains multiple images.
        It calls the extract_markdown_images function with the given text and asserts that
        the returned list of images matches the expected list.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        text = "012![image1](linktoimage1)abc![image2](linktoimage2)xyz"
        images = extract_markdown_images(text)
        self.assertListEqual(
            images,
            [
                ('image1', 'linktoimage1'), 
                ('image2', 'linktoimage3')
            ]
        )

    def test_extract_image_nolink(self):
        """
        Test the extract_markdown_links function when there are no links in the text.

        This function creates a test case where the input text does not contain any links.
        It calls the extract_markdown_links function with the given text and asserts that
        the returned list of links is empty.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        text = "012[link1(url1)abc(url1)xyz"
        links = extract_markdown_links(text)
        self.assertListEqual(
            links,
            []
        )

    def test_extract_image_image(self):
        """
        Test the extract_markdown_links function when there are links in the text.

        This function creates a test case where the input text contains a link.
        It calls the extract_markdown_links function with the given text and asserts that
        the returned list of links matches the expected list.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        text = "012[link1](url1)abc"
        links = extract_markdown_links(text)
        self.assertListEqual(
            links,
            [
                ('link1', 'url1'), 
            ]
        )

    def test_extract_image_multiimage(self):
        """
        Test the extract_markdown_links function when there are multiple links in the text.
        
        This function creates a test case where the input text contains multiple links.
        It calls the extract_markdown_links function with the given text and asserts that
        the returned list of links matches the expected list.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        text = "012[link1](url1)abc[link2](url2)xyz"
        links = extract_markdown_links(text)
        self.assertListEqual(
            links,
            [
                ('link1', 'url1'), 
                ('link2', 'url2')
            ]
        )
        
    def test_split_nodes_image_noimage(self):
        """
        Split nodes into text and image nodes and assert that the resulting list of nodes is equal to the expected list of nodes. 
        The only one node in the input node list does not contain any image.
        
        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.
        
        Returns:
            None
        """
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png and another word", 
            text_type_text,
            )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png and another word", text_type_text, None),
            ]
    ),
        
    def test_split_nodes_image_multiimage(self):
        """
        Test the split_nodes_image function when there is no image in the first node.

        This test case creates one TextNode instance with two images.
        The split_nodes_image function is called with a list containing both nodes.
        The resulting list of nodes is then compared to an expected list of nodes using the assertEqual method.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.
        
        Returns:
            None
        """
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", 
            text_type_text,
            )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", text_type_text, None),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text, None),
                TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
            ]
    ),
        
    def test_split_nodes_image_noimagefirst(self):
        """
        Test the split_nodes_image function when there is no image in the first node.

        This test case creates two TextNode instances, one with no image and another with two images.
        The split_nodes_image function is called with a list containing both nodes.
        The resulting list of nodes is then compared to an expected list of nodes using the assertEqual method.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.
        
        Returns:
            None
        """
        node = TextNode(
            "This is text with an !image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", 
            text_type_text,
            )
        node2 = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", 
            text_type_text,
            )
        new_nodes = split_nodes_image([node, node2])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an !image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", text_type_text, None),
                TextNode("This is text with an ", text_type_text, None),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text, None),
                TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
            ]
    ),


    # External test cases from Boot.dev
        
    def test_split_nodes_image_multinode(self):
        """
        Test the split_nodes_image function when there are multiple nodes with images.

        This test case creates three TextNode instances, each containing different combinations of text and images.
        The split_nodes_image function is called with a list containing all three nodes.
        The resulting list of nodes is then compared to an expected list of nodes using the assertEqual method.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.
        
        Returns:
            None
        """
        node2 = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", 
            text_type_text,
            )
        node0 = TextNode(
            "This is text with an !image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", 
            text_type_text,
            )
        node1 = TextNode(
            "This text also contains an ![image3](http://boot.dev/image.png)", 
            text_type_text,
        )
        new_nodes = split_nodes_image([node2, node0, node1])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", text_type_text, None),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text, None),
                TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
                TextNode("This is text with an !image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)", text_type_text, None),
                TextNode("This text also contains an ", text_type_text, None),
                TextNode("image3", text_type_image, "http://boot.dev/image.png")
            ]
    ),
        
    def test_extract_markdown_images(self):
        """
        Test the extract_markdown_images function when there is one image in the text.

        This function creates a test case where the input text contains one image.
        It calls the extract_markdown_images function with the given text and asserts that
        the returned list of images matches the expected list.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        """
        Test the extract_markdown_links function.

        This function tests the extract_markdown_links function by providing it with a sample input text containing
        markdown links. It calls the extract_markdown_links function with the given text and asserts that the returned
        list of links matches the expected list.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_split_image(self):
        """
        Test the split_nodes_image function when the input node contains a single image.

        This function creates a TextNode instance with text containing a single markdown image.
        It calls the split_nodes_image function with a list containing this node.
        It then asserts that the resulting list of nodes is equal to the expected list of nodes.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        """
        Test the split_nodes_image function when the input node contains a single image.

        This function creates a TextNode instance with text containing a single markdown image.
        It calls the split_nodes_image function with a list containing this node.
        It then asserts that the resulting list of nodes is equal to the expected list of nodes.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        """
        Test the split_nodes_image function when the input node contains multiple images.

        This function creates a TextNode instance with text containing multiple markdown images.
        It calls the split_nodes_image function with a list containing this node.
        It then asserts that the resulting list of nodes is equal to the expected list of nodes.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        """
        Test the split_nodes_link function when the input node contains multiple markdown links.

        This function creates a TextNode instance with text containing multiple markdown links.
        It calls the split_nodes_link function with a list containing this node.
        It then asserts that the resulting list of nodes is equal to the expected list of nodes.

        Parameters:
            self (TestInlineMarkdown): The instance of the TestInlineMarkdown class.

        Returns:
            None
        """
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            new_nodes,
        )
        
    def test_text_to_textnodes(self):
        """
        Test the `text_to_textnodes` function by passing in a sample text string and asserting that the returned list of `TextNode` objects matches the expected list.

        This test case checks if the `text_to_textnodes` function correctly converts the given text string into a list of `TextNode` objects. It verifies that the function correctly identifies and formats different types of inline text, such as bold, italic, code, image, and link.

        The test case passes if the returned list of `TextNode` objects matches the expected list.

        Parameters:
            self: The test case instance.

        Returns:
            None
        """
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
            nodes,
        )

        

if __name__ == "__main__":
    unittest.main()
