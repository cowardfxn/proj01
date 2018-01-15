#!/bin/python
# encoding: utf-8

import numpy as np
from copy import copy

def print_mat(mat):
    print("-" * 8)
    for line in mat:
        print(" ".join([str(e) for e in line]))
    print("=" * 8, "\n")

data = np.unpackbits(np.arange(np.power(2,4)).reshape(-1, 1).astype(np.uint8), axis=1)
samples = data[:, 4:]

local_opt = []
s = 0
for s in range(len(samples)):
    result = []
    for r in range(s, len(samples)):
        cached = []
        valid_row = False
        for c in range(samples.shape[1] - 1):
            for t in range(c+1, samples.shape[1]):
                if (samples[r, c], samples[r, t]) not in cached:
                    valid_row = True
                    cached.append((samples[r, c], samples[r, t]))
        if valid_row:
            result.append(samples[r].tolist())
    if len(result) > len(local_opt):
        local_opt = copy(result)

print_mat(local_opt)
print(len(local_opt))