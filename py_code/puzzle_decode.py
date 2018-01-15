#!/bin/python
# encoding: utf-8

# @contextlib.contextmanager
# define `__enter__` and `__exit__` method in a single function with one yield operation as separator

# https://csedweek.org/resource_kit/blurbs

import string
lowercase = string.ascii_lowercase

i1 = 'vy u wbuhaygueyl vs nyuwbcha iol uwwymm siol jinyhncuf nywb wollcwofog ni mnoxyhnm ch siol wiggohcns '
table1 = str.maketrans("uvwxyzabcdefghijklmnopqrst", "abcdefghijklmnopqrstuvwxyz")
table2 = str.maketrans(lowercase[lowercase.find('u'):]+lowercase[:lowercase.find('u')], lowercase)
s1 = i1.translate(table2)
print(s1)
s2 = ''.join([chr(ord(e) + 4) if e != " " else e for e in s1])
# print(s2)

l2 = []
for e in i1:
    if e != " ":
        chrcd = ord(e) - 20
        if chrcd < 97:
            chrcd = 122 - 96 + chrcd
        l2.append(chr(chrcd))
    else:
        l2.append(e)
s3 = ''.join(l2)
print(s3)
