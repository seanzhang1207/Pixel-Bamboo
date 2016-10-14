#!/usr/bin/python
#coding: utf-8

from modeldata import modeldata
import svgwrite
import cairosvg
from glob import glob
from os.path import basename

GRIDSIZE = 100

layers = [[] for i in range(21)]

for i in range(21):
    for m in modeldata:
        if m['start'][2] == i:
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

    for stick in layer:
        if stick['length'] == 1:
            img.add(img.rect(((stick['start'][0]+1)*GRIDSIZE, (stick['start'][1]+0.5)*GRIDSIZE), (GRIDSIZE, stick['length']*GRIDSIZE), fill='red', stroke='black', stroke_width = GRIDSIZE / 20))
        elif stick['length'] == 2:
            img.add(img.rect(((stick['start'][0]+1)*GRIDSIZE, (stick['start'][1]+0.5)*GRIDSIZE), (GRIDSIZE, stick['length']*GRIDSIZE), fill='green', stroke='black', stroke_width = GRIDSIZE / 20))
        elif stick['length'] == 3:
            img.add(img.rect(((stick['start'][0]+1)*GRIDSIZE, (stick['start'][1]+0.5)*GRIDSIZE), (GRIDSIZE, stick['length']*GRIDSIZE), fill='blue', stroke='black', stroke_width = GRIDSIZE / 20))
    img.save()
    i += 1

for f in glob("blueprint/svg/*.svg"):
    print("Writing image " + "blueprint/png/"+basename(f)[:-4]+".png")
    cairosvg.svg2png(url=f, write_to="blueprint/png/"+basename(f)[:-4]+".png")

print("\nFinished generating blueprints")
