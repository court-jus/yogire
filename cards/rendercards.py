#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import yaml

with open('cards.yml', 'r') as fp:
    cards = yaml.load(fp)

FSIZE = 50
BLACK = Color('#000')
COSTS_X = 650
COSTS_FSIZE = 80

def drawText(draw, txt, x, y):
    #draw.line([0,y],[750,y])
    txt = unicode(txt)
    if not txt:
        return
    nlines = len([t for t in txt.split('\n') if t])
    try:
        shift = [0, 0.5, 1.2, 2.0, 2.5, ][nlines] * FSIZE
    except IndexError:
        shift = 0
    draw.text(x, max(0, int(y - shift)), txt)

for k, v in enumerate(cards):
    filename = '/tmp/card{0:0>2}.png'.format(k)
    with Drawing() as draw:
        with Image(width=750, height=1050) as img:
            draw.fill = BLACK
            draw.rectangle(0, 298, 750, 302)
            draw.rectangle(0, 748, 750, 752)
            draw.rectangle(598, 0, 602, 1050)
            draw.font = 'Robofan.otf'
            draw.gravity = 'north_west'
            draw.font_size = FSIZE
            drawText(draw, v['PE']['text'], 10, 150)
            drawText(draw, v['OSE']['text'], 10, 525)
            drawText(draw, v['EE']['text'], 10, 900)
            draw.font_size = COSTS_FSIZE
            drawText(draw, v['PE']['cost'], COSTS_X, 50)
            drawText(draw, v['PE']['cu'], COSTS_X, 200)
            drawText(draw, v['EE']['str'], COSTS_X, 900)
            drawText(draw, v['OSE']['cost'], COSTS_X, 525)
            draw(img)
            img.save(filename=filename)
        
