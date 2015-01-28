#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import yaml
from random import randrange

with open('attrs.yml', 'r') as fp:
    attrs = yaml.load(fp)

NCARDS=25
used = {
    'OSE': [],
    'PE': [],
    'EE': [],
}
cards = []
OSE = """
01 02 03 04
05 06 07 05 06 07
08 09 10 08 09 10 08 09 10
11 12 13 11 12 13 11 12 13 11 12 13
14 15 14 15 14 15 14 15 14 15
16 16 16 16 16 16
17 17 17 17 17 17 17
""".split()
PE = """
01 02 03 04
05 06 07 06 07 05
08 09 10 09 10 08 08 10 09 11 12 13 14 15 16 11 12 13 14 15 16 11 12 13 14 15 16
17 18 19 17 18 19 17 18 19 17 18 19
20 20 20 20 20
""".split()
EE = """
01 02 03 04 05
06 07 08 09 10
06 07 08 09 10
11 12 13 14 15 16
11 12 13 14 15 16
11 12 13 14 15 16
11 12 13 14 15 16
17 18 19
17 18 19
17 18 19
17 18 19
17 18 19
""".split()
def tofrdct(lst):
    r = {}
    for i in lst:
        r.setdefault(lst.count(i), []).append(i)
    return r
fOSE = tofrdct(OSE)
fPE = tofrdct(PE)
fEE = tofrdct(EE)

maxfr = (max([max(f.keys()) for f in [fOSE, fPE, fEE]]))
for i in range(1, maxfr+1):
    while len(fOSE[i]) > 0:
        ose = fOSE[i].pop()
        j = 0
        while len(fPE.get(j, [])) == 0:
            j += 1
        ipe = randrange(0, len(fPE[j]))
        pe = fPE[j].pop(ipe)
        j = 0
        while len(fEE.get(j, [])) == 0:
            j += 1
        iee = randrange(0, len(fEE[j]))
        ee = fEE[j].pop(iee)
        print(" ".join([ose, pe, ee]))
