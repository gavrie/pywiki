import render

pages = {
    "Main Page": """This is the main page of our Wiki. It has some nice stuff. See the [Second Page] and [Third Page]! """,
    "Second Page": """The second page. See also the [Main Page].""",
    "Third Page": """The third page.""",
}

def render_plain(title):
    return render.render_page(title, pages.get(title, '(empty page)'))

def render_edit(title):
    return render.render_page(title, pages.get(title, ''), edit=True)

def update_contents(title, contents):
    pages[title] = contents
