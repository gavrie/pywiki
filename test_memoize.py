from memoize import cached_calc, calc, cached_liran

def test_calc():
    counter = [0]
    def mycallback(a, b):
        counter[0] = counter[0] + 1

    calc(100, 200, callback=mycallback)
    calc(10, 20, callback=mycallback)
    calc(100, 200, callback=mycallback)

    assert counter[0] == 3

def test_cached_calc():
    counter = [0]
    def mycallback(a, b):
        counter[0] = counter[0] + 1

    calc = cached_calc
    calc(100, 200, callback=mycallback)
    calc(10, 20, callback=mycallback)
    calc(100, 200, callback=mycallback)

    calc = cached_liran
    calc(100, 200, callback=mycallback)
    calc(10, 20, callback=mycallback)
    calc(100, 200, callback=mycallback)

    assert counter[0] == 4

