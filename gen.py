# generator

def foo(seq):
    mylist = list(seq)
    while mylist:
         yield mylist.pop()
