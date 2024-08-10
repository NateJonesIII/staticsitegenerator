from htmlnode import LeafNode

# Define variables for different text types
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    # Class constructor
    def __init__(self,text, text_type, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url
        
    # Checks if the other object is an instance of TextNode.
    def __eq__(self, other):
        # compares all properties in other TextNode
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )

    # Return a string representation of the TextNode object.
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    
    def text_node_to_html_node(self, textNode):
        """
        Convert a TextNode object to an HTML node.

        Parameters:
            textNode (TextNode): The TextNode object to convert.

        Returns:
            LeafNode: An HTML LeafNode representing the TextNode.
        """
        if textNode.text_type == "text":
            return LeafNode(tag=None, value=textNode.value, props=None)
        elif textNode.text_type == "bold":
            return LeafNode(tag="b", value=textNode.value, props=None)
        elif textNode.text_type == "italic":
            return LeafNode(tag="i", value=textNode.value, props=None)
        elif textNode.text_type == "code":
            return LeafNode(tag="code", value=textNode.value, props=None)
        elif textNode.text_type == "link":
            props = {"href": textNode.href}
            return LeafNode(tag="a", value=textNode.value, props=props)
        elif textNode.text_type == "image":
            props = {"src": textNode.src, "alt": textNode.alt}
            return LeafNode(tag="img", value="", props=props)
        else:
            raise ValueError("Invalid text node type")