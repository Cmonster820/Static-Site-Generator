import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_constructor(self):
        node = HTMLNode("a", "meme", [], {})
        self.assertEqual(node.__repr__(), "HTMLNode(a,meme,[],{})")
    
    def test_props_to_html(self):
        node = HTMLNode("a",None,None,{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
    
    def test_children(self):
        node = HTMLNode("a", "meme", [HTMLNode()], {})
        self.assertEqual(node.__repr__(), "HTMLNode(a,meme,[HTMLNode(None,None,None,None)],{})")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_repr(self):
        node = LeafNode(None, "meme",{})
        self.assertEqual(node.__repr__(),"LeafNode(None,meme,{})")

    def test_leaf_a_to_html(self):
        node = LeafNode("a","meme",{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">meme</a>")

if __name__ == "__main__":
    unittest.main()