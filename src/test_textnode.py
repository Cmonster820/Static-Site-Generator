import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("Dummy Node", TextType.text)
        self.assertEqual(node.url, None)
    
    def test_text_type_neq(self):
        node1 = TextNode("Dummy Node", TextType.text)
        node2 = TextNode("Dummy Node Bold", TextType.bold)
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()