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

##################################

def func(*args):
    print "Calculating", args
    return 123

func = memoize(func)

func(1, 2)
func(3, 4)
func(1, 2)
