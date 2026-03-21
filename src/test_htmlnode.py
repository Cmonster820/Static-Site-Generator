import unittest

from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_constructor(self):
        node = HTMLNode("a", "meme", [], {})
        self.assertEqual(node.__repr__(), "HTMLNode(a,meme,[],{})")
    
    def test_props_to_html(self):
        node = HTMLNode("a",None,None,{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
    
    def test_children(self):
        node = HTMLNode("a", "meme", [HTMLNode()], {})
        self.assertEqual(node.__repr__(), "HTMLNode(a,meme,[HTMLNode(None,None,None,None)],{})")

if __name__ == "__main__":
    unittest.main()