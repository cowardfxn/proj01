#!/usr/bin/python
# encoding: utf-8
# csv2json

import json
from collections import OrderedDict
from functools import lru_cache

# @lru_cache(maxsize=None)  OrderedDict unhashable
def name_iter(names, tmp_dict=None):
    if tmp_dict is None:
        tmp_dict = OrderedDict()
    key = names[0]
    if len(names) == 1:
        tmp_dict[key] = "value"
    else:
        try:
            if names[1].startswith("["):
                # when array type
                idx = int(names[1][1:-1])
                tmp_dict.setdefault(key, [OrderedDict() for i in range(idx+1)])
                if idx >= len(tmp_dict[key]):
                    tmp_dict[key] += [OrderedDict() for i in range(idx - len(tmp_dict[key]) + 1)]
                if len(names) == 2:
                    tmp_dict[key][idx] = "value" + names[1]
                else:
                    tmp_dict[key][idx] = name_iter(names[2:], tmp_dict[key][idx])
            else:
                # when object type
                tmp_dict.setdefault(key, OrderedDict())
                tmp_dict[key].update(name_iter(names[1:], tmp_dict[key]))
        except Exception as err:
            print("Error:", err)
    return tmp_dict

d1 = OrderedDict()
name_iter("aa.bb.cc.dd".split("."), d1)
name_iter("aa.bb.cc.ee".split("."), d1)
name_iter("aa.ab.cc".split("."), d1)
name_iter("aa.ab.cd".split("."), d1)
name_iter("bc.bb".split("."), d1)
name_iter("bd".split("."), d1)
name_iter("aa.be".split("."), d1)
name_iter("bc.bf.[0].gg".split("."), d1)
name_iter("bc.bf.[1].cg".split("."), d1)
name_iter("bc.bf.[2].gg".split("."), d1)
name_iter("bc.bf.[3].ge".split("."), d1)

name_iter("bc.bg.[1]".split("."), d1)
name_iter("bc.bg.[3]".split("."), d1)
name_iter("bc.bg.[2]".split("."), d1)
name_iter("bc.bg.[0]".split("."), d1)

print(json.dumps(d1, indent=4))
