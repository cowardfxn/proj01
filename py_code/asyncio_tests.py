#!/bin/python
# encoding: utf-8

import asyncio
import datetime

async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

def example1():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(display_date(loop))
    loop.close()

async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

def example2():
    print("Begin...")
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(slow_operation(future))
    loop.run_until_complete(future)
    print(future.result())
    loop.close()

def get_result(future):
    print(future.result())

def example3():
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(slow_operation(future))
    future.add_done_callback(get_result)
    try:
        loop.run_forever()  # won't stop
    finally:
        print("Run into finally")
        loop.close()


async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task {}: compute factorial({}) ...".format(name, i))
        await asyncio.sleep(1)
        f *= i
    print("Task {}: factorial({}) = {}".format(name, i, f))

def example4():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4))
    )
    loop.close()

if __name__ == '__main__':
    example4()
