from .. import wiki
import pytest

output = """
<h1>Our Nice Wiki</h1>
<h2>Main Page</h2>
<hr>
This is the main page of our Wiki. It has some nice stuff. See the <a href="Second Page">Second Page</a> and <a href="Third Page">Third Page</a>! 
<p>
<hr>
<p><a href="/wiki/Main Page">Main Page</a> | <a href="/edit/Main Page">Edit this page</a></p>
"""

def test_render_page():
    assert wiki.render_page_by_title("Main Page") == output

    with pytest.raises(KeyError):
        assert wiki.render_page_by_title("Foo Bar")
