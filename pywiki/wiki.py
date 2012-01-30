from . import pages
from . import render

def render_page(title):
    print "rendering page {}".format(title)
    return render.render_page(title, pages.get_page(title) or '(empty page)')

def render_page_edit(title):
    return render.render_page(title, pages.get_page(title) or '', edit=True)

def update_page(title, contents):
    pages.set_page(title, contents)

def render_toc():
    return render.render_toc(pages.get_toc())
