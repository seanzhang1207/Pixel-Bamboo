#!/usr/bin/python
#coding: utf-8

# Copyright (c) 2016 Shengchen Zhang

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from __future__ import print_function
from modeldata import modeldata
import svgwrite
import cairosvg
from glob import glob
from os.path import basename


GRIDSIZE = 100

layers = [[] for i in range(21)]

print("Select slicing derection:\n0. X-Axis\n1. Y-Axis\n2. Z-Axis\nInput selection: ", end='')

direction = input()

while direction != 0 and direction != 1 and direction != 2:
    print("Selection doesn't exist. Please re-enter.\nInput selection: ", end='')
    direction = input()

for i in range(21):
    for m in modeldata:
        if m['start'][direction] == i:
            layers[i].append(m)

i = 1
for layer in layers:
    print("Generating... (" + str(i) + "/" + str(len(layers))+")")
    img = svgwrite.Drawing(filename="blueprint/svg/"+str(i)+".svg", size=(23*GRIDSIZE, 23*GRIDSIZE))
    img.add(img.rect((0, 0), (GRIDSIZE*23, GRIDSIZE*23), fill='white'))
    for x in range(21):
        for y in range(21):
            img.add(img.rect(((x+1)*GRIDSIZE, (y+1)*GRIDSIZE), (GRIDSIZE, GRIDSIZE), fill='none', stroke='black', stroke_width = GRIDSIZE / 20))

    for x in range(21):
        img.add(img.text(str(x+1), insert=((x+1.5)*GRIDSIZE, GRIDSIZE-GRIDSIZE/4), text_anchor="middle", font_size = GRIDSIZE/2))

    for y in range(21):
        img.add(img.text(str(y+1), insert=(GRIDSIZE-GRIDSIZE/4, (y+2)*GRIDSIZE-GRIDSIZE/4), text_anchor="end", font_size = GRIDSIZE/2))

    if direction == 0 or direction == 2:
        for stick in layer:
            if stick['length'] == 1:
                img.add(img.rect(((stick['start'][2-direction]+1)*GRIDSIZE, (stick['start'][1]+0.5)*GRIDSIZE), (GRIDSIZE, stick['length']*GRIDSIZE), fill='red', stroke='black', stroke_width = GRIDSIZE / 20))
            elif stick['length'] == 2:
                img.add(img.rect(((stick['start'][2-direction]+1)*GRIDSIZE, (stick['start'][1]+0.5)*GRIDSIZE), (GRIDSIZE, stick['length']*GRIDSIZE), fill='green', stroke='black', stroke_width = GRIDSIZE / 20))
            elif stick['length'] == 3:
                img.add(img.rect(((stick['start'][2-direction]+1)*GRIDSIZE, (stick['start'][1]+0.5)*GRIDSIZE), (GRIDSIZE, stick['length']*GRIDSIZE), fill='blue', stroke='black', stroke_width = GRIDSIZE / 20))
    else:
        for m in modeldata:
            if (i-0.5) >= m['start'][1] and (i-1) < m['start'][1] + m['length']:
                img.add(img.rect(((m['start'][0]+1)*GRIDSIZE, (m['start'][2]+1)*GRIDSIZE), (GRIDSIZE, GRIDSIZE), fill='red', stroke='black', stroke_width = GRIDSIZE / 20))
    img.save()
    i += 1

for f in glob("blueprint/svg/*.svg"):
    print("Writing image " + "blueprint/png/"+basename(f)[:-4]+".png")
    cairosvg.svg2png(url=f, write_to="blueprint/png/"+basename(f)[:-4]+".png")

print("\nFinished generating blueprints")
