#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from __future__ import unicode_literals

import sys
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import yaml
from random import randrange

with open('attrs.yml', 'r') as fp:
    attrs = yaml.load(fp)

repartition = []
with open('repartition.txt', 'r') as fp:
    for line in fp:
        repartition.append(map(int, line.split()))

cards = []
for card in repartition:
    c = {}
    for i, attrname in enumerate(('OSE', 'PE', 'EE')):
        c[attrname] = attrs[attrname][card[i]-1]
    cards.append(c)

with open('cards.yml', 'w') as fp:
    yaml.dump(cards, fp, default_style='|')
