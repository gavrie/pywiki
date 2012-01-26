from .. import pages

def test_page_get():
    mytitle = "A Test Page"
    mycontent = "Some page content..."

    pages.set_page(mytitle, mycontent)
    assert pages.get_page(mytitle) == mycontent

