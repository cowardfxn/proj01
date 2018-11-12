#!/bin/python3
# encoding: utf-8

global a
a = 1234

def get_a():
    return a

def closure_test(i1):
    a = get_a() + 4
    def func(*args):
        print('a in closure: {}'.format(a))
        return args
    return func


def deco(func):
    a = get_a() + 4
    def f(*args):
        # a = args[0]
        print('a in decorator {}'.format(a))
        return func(*args)
    return f

@deco
def decorated(a, b):
    return a + b


if __name__ == '__main__':
    a = 345234
    # closure run, should print latest value of a "345234"
    closure_test(686)()

    a = "RAWWWWW"
    # decorated run, if decorator works like closure, should print "RAWWWWW"
    decorated('s', 'd')
