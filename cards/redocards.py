#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import yaml

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
print(len(OSE), len(PE), len(EE))
