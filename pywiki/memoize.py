def memoize(func):
    cache = {}

    def memoized_func(*args):
        if args in cache:
            result = cache[args]
        else:
            result = func(*args)
            cache[args] = result
        return result

    return memoized_func

