from ..memoize import memoize

def counter():
    count = [0]
    def increment(): count[0] += 1
    def get_count(): return count[0]
    return (increment, get_count)


def test_memoize():

    increment, get_count = counter()

    @memoize
    def foo(a, b):
        increment()
        return a + b

    assert get_count() == 0
    foo(1, 2)
    assert get_count() == 1
    foo(3, 4)
    assert get_count() == 2
    foo(1, 2)
    assert get_count() == 2
