#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import yaml

with open('cards.yml', 'r') as fp:
    cards = yaml.load(fp)

sort_cache = {}
try:
    with open('sort.yml', 'r') as fp:
        sort_cache = yaml.load(fp)
except:
    import traceback
    traceback.print_exc()
    pass

def mk_cmp(k):
    def cmp_attr(a, b):
        if a == b:
            return 0
        print("============ A ==========")
        print(a)
        print("============ B ==========")
        print(b)
        print("=========================")
        if (a, b) in sort_cache[k]:
            return sort_cache[k][(a, b)]
        elif (b, a) in sort_cache[k]:
            return sort_cache[k][(b, a)]
        r = raw_input()
        if r == 'b':
            ret = 1
        else:
            ret = -1
        sort_cache[k][(a, b)] = ret
        return ret
    return cmp_attr

attrs = {}
for attrname in ('OSE','PE','EE'):
    attrs[attrname] = []
    sort_cache.setdefault(attrname, {})
    for k, v in cards.items():
        attrs[attrname].append(v.get(attrname, '').strip())

    try:
        attrs[attrname].sort(mk_cmp(attrname))
    except KeyboardInterrupt:
        with open('sort.yml', 'w') as fp:
            yaml.dump(sort_cache, fp)
        sys.exit(1)

with open('attrs.yml', 'w') as fp:
    yaml.dump(attrs, fp)
with open('sort.yml', 'w') as fp:
    yaml.dump(sort_cache, fp)
