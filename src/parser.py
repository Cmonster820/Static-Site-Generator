from textnode import *

import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type==TextType.text:
            if node.text.count(delimiter)%2!=0:
                raise Exception("invalid md syntax: no closing delimiter found")
            parts = node.text.split(delimiter)
            for i,part in enumerate(parts):
                if i %2 == 0:
                    if part:
                        new_list.append(TextNode(part,TextType.text))
                else:
                    new_list.append(TextNode(part,text_type))
        else:
            new_list.append(node)
    return new_list

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    if len(matches)>0 and not isinstance(matches[0],tuple):
        return [(matches[0],matches[1])]
    return matches


def extract_markdown_images(text):
    pattern = r"!\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(pattern, text)
    if len(matches)>0 and not isinstance(matches[0],tuple):
        return [(matches[0],matches[1])]
    return matches

def split_nodes_link(old_nodes):
    newlist = []
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type==TextType.text:
            parts = re.split(pattern, node.text)
            for i in range(0,len(parts),3):
                if parts[i]:
                    newlist.append(TextNode(parts[i], TextType.text))
                if i + 1 < len(parts):
                    newlist.append(TextNode(parts[i+1], TextType.link, parts[i+2]))
        else:
            newlist.append(node)
    return newlist
    
def split_nodes_image(old_nodes):
    newlist = []
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type==TextType.text:
            parts = re.split(pattern, node.text)
            for i in range(0,len(parts),3):
                if parts[i]:
                    newlist.append(TextNode(parts[i], TextType.text))
                if i + 1 < len(parts):
                    newlist.append(TextNode(parts[i+1], TextType.image, parts[i+2]))
        else:
            newlist.append(node)
    return newlist

def text_to_textnodes(text):
    node = TextNode(text,TextType.text)
    nodes = split_nodes_delimiter([node], "**", TextType.bold)
    nodes = split_nodes_delimiter(nodes, "_", TextType.italic)
    nodes = split_nodes_delimiter(nodes, "`", TextType.code)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes

def markdown_to_blocks(md):
    blocks = md.split("\n\n")
    blocks = [block.strip() for block in blocks if block.strip()]
    return blocks

