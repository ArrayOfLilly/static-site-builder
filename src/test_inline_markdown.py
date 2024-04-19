import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
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
        text = "012[image1](linktoimage1)abc[](linktoimage2)xyz"
        images = extract_markdown_images(text)
        self.assertListEqual(
            images,
            []
        )

    def test_extract_image_image(self):
        text = "012![image1](linktoimage1)abc"
        images = extract_markdown_images(text)
        self.assertListEqual(
            images,
            [
                ('image1', 'linktoimage1'), 
            ]
        )

    def test_extract_image_multiimage(self):
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
        text = "012[link1(url1)abc(url1)xyz"
        links = extract_markdown_links(text)
        self.assertListEqual(
            links,
            []
        )

    def test_extract_image_image(self):
        text = "012[link1](url1)abc"
        links = extract_markdown_links(text)
        self.assertListEqual(
            links,
            [
                ('link1', 'url1'), 
            ]
        )

    def test_extract_image_multiimage(self):
        text = "012[link1](url1)abc[link2](url2)xyz"
        links = extract_markdown_links(text)
        self.assertListEqual(
            links,
            [
                ('link1', 'url1'), 
                ('link2', 'url2')
            ]
        )

if __name__ == "__main__":
    unittest.main()
