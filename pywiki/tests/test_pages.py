from .. import pages

import pytest

def test_setting_a_page_and_then_getting_it_returns_the_correct_content():
    mytitle = "A Test Page"
    mycontent = "Some page content..."

    pages.set_page(mytitle, mycontent)
    assert pages.get_page(mytitle) == mycontent

def test_updating():
    mytitle = "A Test Page"
    mycontent2 = "Some page content (updated)..."
    pages.set_page(mytitle, mycontent2)
    assert pages.get_page(mytitle) == mycontent2

def test_getting_a_nonexistent_page_fails():
    with pytest.raises(KeyError):
        assert pages.get_page("Foo Bar")
