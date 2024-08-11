import unittest
from main import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_h1_header_present(self):
        markdown = "# Hello World"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello World")

    def test_h1_header_with_extra_whitespace(self):
        markdown = "  #   Hello World   "
        result = extract_title(markdown)
        self.assertEqual(result, "Hello World")

    def test_h1_header_not_present(self):
        markdown = "## Hello World"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), 'No h1 header was found')

    def test_multiple_lines(self):
        markdown = """
        # Title
        Some content
        ## Subtitle
        """
        result = extract_title(markdown)
        self.assertEqual(result, "Title")

    def test_no_header_raises_exception(self):
        markdown = "This is just text without any header."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), 'No h1 header was found')

    def test_empty_string(self):
        markdown = ""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), 'No h1 header was found')

if __name__ == '__main__':
    unittest.main()
