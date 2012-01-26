def func(*args):
    print "Calculating", args
    return 123

cache = {}

def memoized_func(*args):
    if args in cache:
        result = cache[args]
    else:
        result = func(*args)
        cache[args] = result
    return result


memoized_func(1, 2)
memoized_func(3, 4)
memoized_func(1, 2)
