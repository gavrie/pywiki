def memoize(f):
    cache = {}

    def memoized_f(*args):
        if args in cache:
            result = cache[args]
        else:
            result = f(*args)
            cache[args] = result
        return result

    return memoized_f

##################################

def func(*args):
    print "Calculating", args
    return 123

func = memoize(func)

func(1, 2)
func(3, 4)
func(1, 2)
