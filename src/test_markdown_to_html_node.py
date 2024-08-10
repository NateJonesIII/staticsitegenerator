import unittest

from block_markdown import *

def test_markdown_to_html_node():
    markdown = "# Heading\n\nThis is a paragraph.\n\n- List item 1\n- List item 2"
    html_node = markdown_to_html_node(markdown)
    
    assert html_node.tag == 'div'
    assert len(html_node.children) == 3
    assert html_node.children[0].tag == 'h1'
    assert html_node.children[1].tag == 'p'
    assert html_node.children[2].tag == 'ul'
