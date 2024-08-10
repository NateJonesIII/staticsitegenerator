import unittest
from textnode import (TextNode,text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_not_eq_different_text(self):
        # Test inequality when text properties are different
        node = TextNode("This is a text node", "bold", "https://example.com")
        node2 = TextNode("This is another text node", "bold", "https://example.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_text_type(self):
        # Test inequality when text_type properties are different
        node = TextNode("This is a text node", "bold", "https://example.com")
        node2 = TextNode("This is a text node", "italic", "https://example.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_url(self):
        # Test inequality when url properties are different
        node = TextNode("This is a text node", "bold", "https://example.com")
        node2 = TextNode("This is a text node", "bold", "https://example.org")
        self.assertNotEqual(node, node2)
    """
    def test_not_eq_different_types(self):
        # Test inequality when comparing TextNode with different types
        node = TextNode("This is a text node", "bold", "https://example.com")
        not_a_node = "This is not a TextNode"

        try:
            # Attempt to compare node with not_a_node
            self.assertNotEqual(node, not_a_node)
        except AttributeError as e:
            # Raise a more informative error message
            raise TypeError("Comparison with a non-TextNode object is not supported.") from e
    """
    def test_repr(self):
        # Test the string representation of TextNode objects
        node = TextNode("This is a text node", "bold", "https://example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://example.com)")

    def test_repr_empty_text(self):
        # Test the string representation of TextNode object with empty text
        node = TextNode("", "bold", "https://example.com")
        self.assertEqual(repr(node), "TextNode(, bold, https://example.com)")

    def test_repr_empty_text_type(self):
        # Test the string representation of TextNode object with empty text_type
        node = TextNode("This is a text node", "", "https://example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, , https://example.com)")

    def test_repr_none_text_type(self):
        # Test the string representation of TextNode object with None text_type
        node = TextNode("This is a text node", None, "https://example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, None, https://example.com)")


if __name__ == "__main__":
    unittest.main()
