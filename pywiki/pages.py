class Page(object):

    def __init__(self, title, content):
        self._title = title
        self._content = content

    @property
    def content(self):
        print "fetching content"
        return self._content

    @property
    def title(self):
        return self._title

    def __repr__(self): # representation
        return "<Page '{}'>".format(self.title)

    def __str__(self): # string representation
        return "Wiki Page: '{}'".format(self.title)


class PageCollection(object):
    def __init__(self):
        self._pages = {}

    def __setitem__(self, title, content):
        self._pages[title] = Page(title, content)

    def __getitem__(self, title):
        return self._pages[title].content

#######################################

pages = PageCollection()

pages["Main Page"] = """This is the main page of our Wiki. It has some nice stuff. See the [Second Page] and [Third Page]! """
pages["Second Page"] = """The second page. See also the [Main Page]."""
pages["Third Page"] = """The third page."""

def get_page(title):
    return pages[title]

def set_page(title, content):
    pages[title] = content
