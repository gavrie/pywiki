class Page(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return "<Page '{}'>".format(self.title)


class PageIterator(object):
    def __init__(self, pages):
        self._pages = pages
        self._keys = list(pages.keys())

    def next(self):
        try:
            return self._pages[self._keys.pop()]
        except IndexError:
            raise StopIteration


class PageCollection(object):
    def __init__(self):
        self._pages = { 
            "first":  Page("first", "foo"),
            "second": Page("second", "bar"),
        }

    def __setitem__(self, title, content):
        self._pages[title] = Page(title, content)

    def get(self, title):
        return self._pages[title].content

    def __iter__(self):
        return PageIterator(self._pages)

#######################################

pages = PageCollection()

pages["Main Page"] = """This is the main page of our Wiki. It has some nice stuff. See the [Second Page] and [Third Page]! """
pages["Second Page"] = """The second page. See also the [Main Page]."""
pages["Third Page"] = """The third page."""

def get_page(title):
    return pages.get(title)

def set_page(title, content):
    pages[title] = content
