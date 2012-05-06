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

def test_rendering_a_page_by_title_returns_the_expected_output():
    assert wiki.render_page_by_title("Main Page") == output

def test_rendering_a_nonexistent_page_fails_with_an_exception():
    with pytest.raises(KeyError):
        assert wiki.render_page_by_title("Foo Bar")
