from . import pages
from . import render
from .memoize import memoize

@memoize
def render_page(title):
    print "rendering page {}".format(title)
    return render.render_page(title, pages.get_page(title) or '(empty page)')

def render_page_edit(title):
    return render.render_page(title, pages.get_page(title) or '', edit=True)

def update_page(title, contents):
    pages.set_page(title, contents)
