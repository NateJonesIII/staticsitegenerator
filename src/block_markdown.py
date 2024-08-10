import re

from htmlnode import HTMLNode, ParentNode

# Define variables for different block types
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    # Split the input text into distinct blocks using whitespace as the delimiter
    blocks = markdown.split("\n\n")
    # Strip leading and trailing whitespace from each block storage list
    stripped_blocks = []
    
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        stripped_blocks.append(block)
    return stripped_blocks
        



def block_to_block_type(block):
        lines = block.split("\n")
        
        # Heading type return
        if (
            block.startswith("# ")
            or block.startswith("## ")
            or block.startswith("### ")
            or block.startswith("#### ")
            or block.startswith("##### ")
            or block.startswith("###### ")
        ):
            return block_type_heading
        
         # Code block
        if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
            return block_type_code
        
        # Quote block
        if block.startswith(">"):
            for line in lines:
                if not line.startswith(">"):
                    return block_type_paragraph
            return block_type_quote
        
        # Unordered list block
        if block.startswith("* "):
            for line in lines:
                if not line.startswith("* "):
                    return block_type_paragraph
            return block_type_unordered_list
        
        # Ordered list block
        if block.startswith("- "):
            for line in lines:
                if not line.startswith("- "):
                    return block_type_paragraph
            return block_type_unordered_list
        
        # Default to paragraph
        if block.startswith("1. "):
            i = 1
            for line in lines:
                if not line.startswith(f"{i}. "):
                    return block_type_paragraph
                i += 1
            return block_type_ordered_list
        return block_type_paragraph
    
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def create_list_node(block, list_type):
    list_node = HTMLNode(list_type)
    items = block.split('\n')
    for item in items:
        item_text = item.lstrip('-*1234567890. ').strip()
        list_node.add_child(HTMLNode('li', children=text_to_children(item_text)))
    return list_node

    
def markdown_to_html_node(markdown):
    # Split the markdown into blocks (you already have a function for this)
    blocks = markdown_to_blocks(markdown)
    
    # Step 2: Initialize the root HTML node (e.g., a <div>)
    root_node = HTMLNode('div')
    
    # Step 3: Loop over each block and convert it to an HTMLNode
    for block in blocks:
        # Determine the type of block and create the appropriate HTMLNode
        block_type = determine_block_type(block)
        block_node = create_html_node(block, block_type)
        
        # Add the block node as a child of the root node
        root_node.add_child(block_node)
    
    return root_node

def create_html_node(block, block_type):
    if block_type == 'heading':
        level = block.count('#', 0, block.index(' '))  # Count number of # characters
        return HTMLNode(f'h{level}', text=block.lstrip('# ').strip())
    elif block_type == 'quote':
        return HTMLNode('blockquote', children=text_to_children(block.lstrip('> ').strip()))
    elif block_type == 'unordered_list':
        return create_list_node(block, 'ul')
    elif block_type == 'ordered_list':
        return create_list_node(block, 'ol')
    elif block_type == 'code_block':
        return HTMLNode('pre', children=[HTMLNode('code', text=block.strip('```'))])
    else:
        return HTMLNode('p', children=text_to_children(block))


def create_list_node(block, list_type):
    list_node = HTMLNode(list_type)
    items = block.split('\n')
    for item in items:
        item_text = item.lstrip('-*1234567890. ').strip()
        list_node.add_child(HTMLNode('li', children=text_to_children(item_text)))
    return list_node
