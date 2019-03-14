#!/bin/python
# coding: utf-8

import numpy as np


def fast_sort(input_array, sort_start=0, sort_end=None):
    result = list(input_array)
    if sort_end is None:
        sort_end = len(result) - 1

    if sort_start == sort_end or (sort_end + 1) - sort_start < 2:
        return result

    base_val = result[sort_start]
    idx_se, idx_be = sort_start, sort_end or (len(result) - 1)

    while idx_se < idx_be:
        # iterate from big endian first
        if result[idx_be] < base_val:
            # start iterating from small endian
            idx_se += 1
            if result[idx_se] > base_val:
                # swap small endian and big endian values
                result[idx_se], result[idx_be] = result[idx_be], result[idx_se]
                # continue iterating over big endian
                idx_be = idx_be - 1
            else:
                # else, continue iterating over small endian
                pass
        else:
            # else, continue iterating over big endian
            idx_be = idx_be - 1

    # swap median value and base value
    result[sort_start], result[idx_se] = result[idx_se], result[sort_start]

    # print(result, idx_se, idx_be, sort_start, sort_end)

    result = fast_sort(result, sort_start=sort_start, sort_end=idx_be)
    result = fast_sort(result, sort_start=idx_be + 1, sort_end=sort_end)

    return result


def test():
    for i in range(1000):
        l1 = np.random.randint(1, 1000, 10)
        l2 = fast_sort(l1)
        l3 = sorted(l1)
        if l2 != l3:
            print("Exception\nfast sort output: {},\nsorted output: {}".format(l2, l3))
    print('Done')


if __name__ == "__main__":
    print(fast_sort([3, 7, 3, 1, 9, 4, 9, 7, 5, 5]))

    test()
