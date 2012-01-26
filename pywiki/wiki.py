from . import pages
from . import render

def render_page_by_title(title):
    return render.render_page(title, pages.get_page(title) or '(empty page)')
