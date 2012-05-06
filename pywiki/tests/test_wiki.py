from .. import wiki

output = """
<h1>Our Nice Wiki</h1>
<h2>Main Page</h2>
<hr>
This is the main page of our Wiki. It has some nice stuff. See the <a href="Second Page">Second Page</a> and <a href="Third Page">Third Page</a>! 
<p>
<hr>
<p>
   <a href="/wiki/Main Page">Main Page</a> | 
   <a href="/edit/Main Page">Edit this page</a>
</p>
"""

def test_rendering_a_page_returns_the_expected_output():
    assert wiki.render_page("Main Page") == output

def test_rendering_a_nonexistent_page_returns_an_empty_page():
    assert '(empty page)' in wiki.render_page("Foo xxx Bar")
