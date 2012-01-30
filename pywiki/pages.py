class Page(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content

class PageCollection(object):
    def __init__(self):
        self._pages = {}

    def __setitem__(self, title, content):
        self._pages[title] = Page(title, content)

    def get(self, title):
        if title in self._pages:
            return self._pages[title].content
        else:
            return ""

    def get_titles(self):
        for page in self._pages:
            yield page.title()

#######################################

pages = PageCollection()

pages["Main Page"] = """This is the main page of our Wiki. It has some nice stuff. See the [Second Page] and [Third Page]! """
pages["Second Page"] = """The second page. See also the [Main Page]."""
pages["Third Page"] = """The third page."""

def get_page(title):
    return pages.get(title)

def set_page(title, content):
    pages[title] = content

def get_toc():
    return pages.get_titles()
