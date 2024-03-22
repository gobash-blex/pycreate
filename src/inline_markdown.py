import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """This function takes a list of nodes, a delimiter, and a text type as arguments. Returns a new list of nodes where nodes with delimiters become the intended text type."""
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter) 
        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown Syntax, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    regex_pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex_pattern, text)
    return matches

def extract_markdown_links(text):
    regex_pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex_pattern, text)
    return matches