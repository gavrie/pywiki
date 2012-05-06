from .. import render

def cleanup(text):
    return "\n".join(l.strip() for l in text.splitlines())

def test_rendering_a_page_returns_the_expected_result():
    title = "Test Page"
    contents = "Some nice text with a [Linked Page].\nAnd more text."
    result = """
<h1>Our Nice Wiki</h1>
<h2>Test Page</h2>
<hr>
Some nice text with a <a href="Linked Page">Linked Page</a>.
And more text.
<p>
<hr>
<p>
<a href="/wiki/Main Page">Main Page</a> |
<a href="/edit/Test Page">Edit this page</a>
</p>\
"""

    assert cleanup(render.render_page(title, contents)) == result
