def cb_print(*args):
    print "calc:", args



def memoize(func):

    cache = {}

    def cached_func(*args, **kwargs):
        key = args
        if not key in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return cached_func


@memoize
def calc(*args, **kwargs):
    callback = kwargs.get('callback')
    if callback:
        callback(*args)
    a, b = args
    return a * b



@memoize
def liran_calc(*args, **kwargs):
    callback = kwargs.get('callback')
    if callback:
        callback(*args)
    a, b = args
    return a / b







