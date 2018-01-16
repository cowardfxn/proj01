#!/bin/python3
# encoding: utf-8

import asyncio


# generator sample
def lazy_range(up_to):
    index = 0
    def gratuitous_refactor():
        nonlocal index
        while index < up_to:
            yield index
            index += 1
    yield from gratuitous_refactor()

async def coro1():
    await lazy_range(1000)

# coroutine function, returns a coroutine, which is not iterable
@asyncio.coroutine
def coro2():
    yield from lazy_range(100)

if __name__ == '__main__':
    coro1()

    try:
        for e in coro1():
            print(e)
    except TypeError as te:
        print("Error: {}".format(te))

    # generator1 = lazy_range(100)
    # for i in range(22):
    #     a = next(generator1)
    # for i in range(10):
    #     print(next(generator1))
