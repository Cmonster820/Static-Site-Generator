from textnode import *
from htmlnode import *
from conversions import *
from parser import *
import unittest

class TestParser(unittest.TestCase):
    def test_bold(self):
        node = TextNode("There is some **bold** text here",TextType.text)
        nodes = split_nodes_delimiter([node],"**",TextType.bold)
        self.assertEqual(nodes, [TextNode("There is some ",TextType.text),TextNode("bold",TextType.bold),TextNode(" text here",TextType.text)])
    
    def test_italic(self):
        node = TextNode("There is some _italic_ text here",TextType.text)
        nodes = split_nodes_delimiter([node],"_",TextType.italic)
        self.assertEqual(nodes, [TextNode("There is some ",TextType.text),TextNode("italic",TextType.italic),TextNode(" text here",TextType.text)])
    
    def test_code(self):
        node = TextNode("There is some `code` text here",TextType.text)
        nodes = split_nodes_delimiter([node],"`",TextType.code)
        self.assertEqual(nodes, [TextNode("There is some ",TextType.text),TextNode("code",TextType.code),TextNode(" text here",TextType.text)])
    
    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted = extract_markdown_links(text)
        self.assertEqual(extracted, [("to boot dev", "https://www.boot.dev"),("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("link", TextType.link, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.text),
                TextNode(
                    "second link", TextType.link, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_no_links(self):
        node = TextNode("This is text with no links.", TextType.text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [node])

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.text),
                TextNode("image", TextType.image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.text),
                TextNode(
                    "second image", TextType.image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_multiple_images(self):
        node = TextNode("Image one ![one](https://example.com/one.png) and image two ![two](https://example.com/two.png)", TextType.text)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("Image one ", TextType.text),
            TextNode("one", TextType.image, "https://example.com/one.png"),
            TextNode(" and image two ", TextType.text),
            TextNode("two", TextType.image, "https://example.com/two.png")
        ])
    
    def test_no_images(self):
        node = TextNode("This is text with no images.", TextType.text)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])

    def test_all_func(self):
        nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(nodes,[
                                TextNode("This is ", TextType.text),
                                TextNode("text", TextType.bold),
                                TextNode(" with an ", TextType.text),
                                TextNode("italic", TextType.italic),
                                TextNode(" word and a ", TextType.text),
                                TextNode("code block", TextType.code),
                                TextNode(" and an ", TextType.text),
                                TextNode("obi wan image", TextType.image, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                TextNode(" and a ", TextType.text),
                                TextNode("link", TextType.link, "https://boot.dev"),
                            ])
        
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    

if __name__ == "__main__":
    unittest.main()