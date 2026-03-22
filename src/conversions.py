from textnode import *
from htmlnode import *

class Conversions:
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.text:
                return LeafNode(None, text_node.text)
            case TextType.bold:
                return LeafNode("b", text_node.text)
            case TextType.italic:
                return LeafNode("i", text_node.text)
            case TextType.code:
                return LeafNode("code", text_node.text)
            case TextType.link:
                return LeafNode("a", text_node.text, {"href":text_node.url})
            case TextType.image:
                return LeafNode("img", "", {"src":text_node.url,"alt":text_node.text})
            