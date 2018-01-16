#!/bin/python3
# encoding: utf-8

import heapq
import types
import time
from datetime import datetime, timedelta

class Task:
    """
    Represents how long a coroutine should wait before starting again,
    Comparision operators are implemented for use by heapq. Tow-item tuples unfortunately don't work
    because when the datetime.datetime instances are equal, comparision falls to the coroutne and they
    don't implement comparision methods, triggering an exception.

    Think of this as being like asyncio.Task/curio.Task.
    """
    def __init__(self, wait_until, coro):
        self.coro = coro
        self.wait_until = wait_until

    def __eq__(self, other):
        return self.wait_until == other.wait_until

    def __lt__(self, other):
        return self.wait_until < other.wait_until

class SleepingLoop:
    """
    An event loop focused on delaying execution of coroutines.

    Think of this as being like asyncio.BaseEventloop/curio.Kernel.
    """
    def __init__(self, *coros):
        self._new = coros
        self._waiting = []

    def run_until_complete(self):
        # start all the coroutines
        for coro in self._new:
            wait_for = coro.send(None)
            heapq.heappush(self._waiting, Task(wait_for, coro))
        # keep running until there is no more work to do
        while self._waiting:
            now = datetime.now()
            # get the coroutines with the soonest resumption time
            task = heapq.heappop(self._waiting)
            if now < task.wait_until:
                # We're ahead of shedule, wait until it's time to resume
                delta = task.wait_until - now
                time.sleep(delta.total_seconds())
                now = datetime.now()
            try:
                # It's time to resume the coroutine
                wait_until = task.coro.send(now)
                heapq.heappush(self._waiting, Task(wait_until, task.coro))
            except StopIteration:
                # The coroutine is done.
                pass


@types.coroutine
def sleep(seconds):
    """
    Pause the coroutine for a specific number of seconds.

    Think of this as being like asyncio.sleep/curio.sleep.
    """
    now = datetime.now()
    wait_until = now + timedelta(seconds=seconds)
    # Make all the coroutines on the call stack pause, the need to use 'yield' necessitates this
    # be generator-based and not async-based coroutine.
    actual = yield wait_until
    # Resume the execution stack, sending back how long we actually waited.
    return actual - now


async def countdown(label, length, *, delay=0):
    """
    Countdown a launch for `length` seconds, waiting `delay` seconds.

    This is what a user would typically write.
    """
    print(label, 'waiting', delay, 'seconds before starting countdown.')
    delta = await sleep(delay)
    print(label, 'starting after waiting', delta)
    while length:
        print(label, 'T-minus', length)
        waited = await sleep(1)
        length -= 1
    print('label', 'list-off!')

def main():
    """
    Starting the event loop, counting down 3 separate launches.

    This is what a user would typically write.
    """
    loop = SleepingLoop(countdown('A', 5), countdown('B', 3, delay=2), countdown('C', 4, delay=1))
    start = datetime.now()
    loop.run_until_complete()
    print('Total elapsed time is', datetime.now() - start)


if __name__ == '__main__':
    main()
