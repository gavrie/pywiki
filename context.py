from contextlib import contextmanager

@contextmanager
def locker():
    print "Acquiring lock"
    try:
        yield
    finally:
        print "Releasing lock"

################################

def main():
    print "Going to do something with lock"

    with locker():
        print "We are locked now"
        raise IndexError
        print "We are still locked"

    print "No longer locked"


main()
