import pages

def cleanup(text):
    return "\n".join(l.strip() for l in text.splitlines())

class TestPages(object):
    def test_page(self):
        assert cleanup(pages.render_plain("Third Page")) == """
<h1>Our Nice Wiki</h1>
<h2>Third Page</h2>
<hr>
The third page.
<p>
<hr>
<p><a href="/wiki/Main Page">Main Page</a> | <a href="/edit/Third Page">Edit this page</a></p>
"""
