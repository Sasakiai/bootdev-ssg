import unittest

from markdown_parser import markdown_to_html_node


class MarkdownParserTests(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_heading(self):
        md = """
# This is a heading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1></div>",
        )

    def test_heading_levels(self):
        md = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></div>",
        )

    def test_heading_with_formatting(self):
        md = """
# Heading with **bold** and _italic_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading with <b>bold</b> and <i>italic</i></h1></div>",
        )

    def test_quote(self):
        md = """
> This is a quote
> that spans multiple
> lines
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote that spans multiple lines</blockquote></div>",
        )

    def test_quote_with_formatting(self):
        md = """
> This is a quote with **bold** text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <b>bold</b> text</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- this is
- unordered
- list
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>this is</li><li>unordered</li><li>list</li></ul></div>",
        )

    def test_unordered_list_with_formatting(self):
        md = """
- item with **bold**
- item with _italic_
- item with `code`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>item with <b>bold</b></li><li>item with <i>italic</i></li><li>item with <code>code</code></li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. first
2. second
3. third
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first</li><li>second</li><li>third</li></ol></div>",
        )

    def test_ordered_list_with_formatting(self):
        md = """
1. item with **bold**
2. item with _italic_
3. item with `code`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>item with <b>bold</b></li><li>item with <i>italic</i></li><li>item with <code>code</code></li></ol></div>",
        )

    def test_full_document(self):
        md = """
# Heading Here

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

```
This is text that _should_ remain
the **same** even with inline stuff
```

- this is
- unordered
- list

1. And this
2. is ordered
3. list with **some**
4. **formatting** here _too_

> This is a quote
> that spans multiple
> lines and has **bold** text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("<h1>Heading Here</h1>", html)
        self.assertIn("<b>bolded</b>", html)
        self.assertIn("<i>italic</i>", html)
        self.assertIn("<code>code</code>", html)
        self.assertIn("<pre><code>", html)
        self.assertIn("<ul>", html)
        self.assertIn("<ol>", html)
        self.assertIn("<blockquote>", html)
        self.assertTrue(html.startswith("<div>"))
        self.assertTrue(html.endswith("</div>"))


if __name__ == "__main__":
    unittest.main()
