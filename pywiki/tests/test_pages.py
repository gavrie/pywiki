from .. import pages

def test_setting_a_page_and_then_getting_it_returns_the_correct_content():
    mytitle = "A Test Page"
    mycontent = "Some page content..."

    pages.set_page(mytitle, mycontent)
    assert pages.get_page(mytitle) == mycontent
