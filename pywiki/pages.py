pages = {
    "Main Page": """This is the main page of our Wiki. See the [Second Page] and [Third Page]!""",
    "Second Page": """The second page. See also the [Main Page].""",
    "Third Page": """The third page.""",
}

def get_page(title):
    return pages[title]

def set_page(title, content):
    pages[title] = content
