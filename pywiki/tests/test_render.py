from .. import render

def cleanup(text):
    return "\n".join(l.strip() for l in text.splitlines())

def test_page():
    title = "Test Page"
    contents = "Some nice text."
    result = """
<h1>Our Nice Wiki</h1>
<h2>Test Page</h2>
<hr>
Some nice text.
<p>
<hr>
<p><a href="/wiki/Main Page">Main Page</a> | <a href="/edit/Test Page">Edit this page</a></p>\
"""

    assert cleanup(render.render_page(title, contents)) == result
