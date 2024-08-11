import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # Initialize a new list to store the split nodes
    new_nodes = []
    
    # Iterate through each node in the old_nodes list
    for old_node in old_nodes:
        
        # If an "oldnode" is not a text type TextNode, you should just add it to the new list as-is, we only attempt to split text type TextNode objects.
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        # Initialize a list to store the split nodes
        split_nodes = []
        
        # Split the text of the current node using the specified delimiter
        sections = old_node.text.split(delimiter)
        
        # Check if the number of sections is odd, indicating an invalid markdown format
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        # Iterate through each section of the split text
        for i in range(len(sections)):
            # Skip empty sections
            if sections[i] == "":
                continue
            # Create a new TextNode for each non-empty section
            if i % 2 == 0:
                # For even-indexed sections, use the specified text type
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                # For odd-indexed sections, use the provided text type
                split_nodes.append(TextNode(sections[i], text_type))
        """ 
        Extend the new_nodes list with the split nodes
        The extend() method in `Python` is used to add elements from one list (or any iterable) to the end of another list.
        """
        new_nodes.extend(split_nodes)
    # Return the list of split nodes
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    # Initialize a new list to store the split nodes
    new_nodes = []
    
    # Iterate through each node in the old_nodes list
    for old_node in old_nodes:
        # Check if the node is not of type text
        if old_node.text_type != text_type_text:
            # If not, simply append the node to new_nodes and continue to the next node
            new_nodes.append(old_node)
            continue
        
        # Store the original text of the current node
        original_text = old_node.text
        
        # Extract images from the original text using the extract_markdown_images function
        images = extract_markdown_images(original_text)
        
        # If no images are found in the text, append the original node to new_nodes and continue
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        
        # Iterate through each image found in the text
        for image in images:
            # Split the original text into sections before and after the current image
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            
            # Check if the split resulted in exactly two sections, indicating a valid image markdown
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            
            # If there is text before the image, create a new text node and append it to new_nodes
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            
            # Create a new text node for the current image and append it to new_nodes
            new_nodes.append(
                TextNode(
                    image[0],  # Alt text of the image
                    text_type_image,  # Text type indicating it's an image
                    image[1],  # URL of the image
                )
            )
            
            # Update the original text to the section after the current image
            original_text = sections[1]
        
        # If there is remaining text after all images have been processed, create a text node for it and append it to new_nodes
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    
    # Return the list of split nodes
    return new_nodes


    
def split_nodes_link(old_nodes):
    # Initialize a new list to store the split nodes
    new_nodes = []
    
    # Iterate through each node in the old_nodes list
    for old_node in old_nodes:
        # If the current node is not a text type TextNode, add it to the new list as-is
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        # Get the original text from the current node
        original_text = old_node.text
        
        # Extract markdown links from the original text
        links = extract_markdown_links(original_text)
        
        # If there are no links in the text, add the current node to the new list and continue
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        
        # Iterate through each link extracted from the text
        for link in links:
            # Split the original text into sections based on the current link
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            
            # Check if the split resulted in exactly two sections, indicating a valid link format
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            
            # If there is text before the link, add it to the new list as a text node
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            
            # Add the current link as a TextNode to the new list
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            
            # Update the original text to the remaining part after the link
            original_text = sections[1]
        
        # If there is remaining text after processing all links, add it to the new list as a text node
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    
    # Return the list of split nodes
    return new_nodes

def text_to_textnodes(text):
    # List to store text_nodes
    to_text_nodes = []
    
    # Split text into text nodes using each splitting function
    text_nodes = [TextNode(text, text_type_text)]
    text_nodes = split_nodes_delimiter(text_nodes, "**", text_type_bold)
    text_nodes = split_nodes_delimiter(text_nodes, "*", text_type_italic)
    text_nodes = split_nodes_delimiter(text_nodes, "`", text_type_code)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    
    # Extend the list of nodes with the resulting text nodes
    to_text_nodes.extend(text_nodes)
    
    return to_text_nodes