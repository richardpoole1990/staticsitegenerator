import unittest
from page_generator import extract_title  # replace with your actual module name


class TestExtractTitle(unittest.TestCase):

    def test_basic_title(self):
        markdown = "# Hello World\nThis is some content."
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_title_with_extra_spaces(self):
        markdown = "#    Spaced Title    \nMore content."
        self.assertEqual(extract_title(markdown), "Spaced Title")

    def test_no_title(self):
        markdown = "This has no title\nJust content."
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_only_subheadings(self):
        markdown = "## This is a subheading\n### Another subheading"
        with self.assertRaises(ValueError):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()