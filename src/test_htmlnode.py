import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        dict = {"class": "test-div", "label": "Test label"}
        node = HTMLNode("div", "Test div", None, dict)

        test_correct = ' class="test-div" label="Test label"'
        self.assertEqual(node.props_to_html(), test_correct)

    def test_not_eq(self):
        node = HTMLNode("div", "Test div", None, None)
        self.assertNotEqual(node.props_to_html(), ' class="test"')
