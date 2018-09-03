#!/bin/python3
# encoding: utf-8

import sys
import numpy as np
from time import time

'''
x
[0, 2] => idx start 0, end 3
[3, 5] => idx start 3, end 6
[6, 8] => idx start 6, end 9

((0 + (r_idx // 3 * 3)): (3 + (r_idx // 3 * 3)), (0 + (c_idx // 3 * 3)): (3 + (c_idx // 3 * 3)))

np.random.randint(1, 10)
'''

sys.setrecursionlimit(10 ** 7)

np.random.seed(int(time() % 1000))
TRIALS = [(0, 0, 0)]

def padding(input_values, rollback=False):
    MAX_ROW, MAX_COL = input_values.shape
    # if it is rollback
    if rollback:
        if len(TRIALS) == 0:
            raise Exception('No possible result!')

        i, j, prev_val = TRIALS.pop()
        valid_digit = False
        for num in range(prev_val+1, 10):
            input_values[i, j] = num
            valid_digit = value_chk(input_values, i, j)
            if valid_digit:  # if value fits current position
                TRIALS.append((i, j, num))
                return padding(input_values)
        if not valid_digit:  # if not updated
            # clear value
            input_values[i, j] = 0
            # and rollback again
            return padding(input_values, True)
    else:
        # if new position
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if input_values[i, j] == 0:
                    valid_digit = False
                    for num in range(1, 10):
                        input_values[i, j] = num
                        valid_digit = value_chk(input_values, i, j)
                        if valid_digit:  # if value fits current position
                            TRIALS.append((i, j, num))
                            return padding(input_values)
                    # if no digit fits, rollback
                    if not valid_digit:
                        input_values[i, j] = 0
                        return padding(input_values, True)

    return input_values



def value_chk(val_mtx, row_idx, col_idx):
    val = val_mtx[row_idx, col_idx]
    return (dup_cnt(val_mtx[row_idx, :], val) == 1
        and dup_cnt(val_mtx[:, col_idx], val) == 1
        and dup_cnt(val_mtx[(0 + (row_idx // 3 * 3)): (3 + (row_idx // 3 * 3)), (0 + (col_idx // 3 * 3)): (3 + (col_idx // 3 * 3))].flatten(), val) == 1)

def dup_cnt(tar_arr, val):
    cnt = 0
    for e in tar_arr:
        if e == val:
            cnt += 1
    return cnt

if __name__ == '__main__':
    i1 = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])
    print('Original input:\n', i1)
    result = padding(i1)
    print('Result:\n', result)

    # result check
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if not value_chk(result, i, j):
                raise Exception("Unvalid result! ({}, {})".format(i, j))
