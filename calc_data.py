#!/usr/local/bin/python3
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

from model import Model
from graphs import crab, lotus

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

MODELSIZE = 21
PATH_TO_MAYA_SCRIPT = "/Users/Sean/Library/Preferences/Autodesk/maya/2016/prefs/scriptEditorTemp/gen_model.py"

fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(111, projection='3d')
#ax2 = fig.add_subplot(111, projection='3d')
print("Model size is set to: " + str(MODELSIZE) + "x" + str(MODELSIZE) + ". Calculating...")
model = Model(MODELSIZE, crab, lotus)



#print(model.matrix)

#print(model.ys.reverse())

#for x in range(model.size):
#    for y in range(model.size):
#        ax.text(0, x/float(model.size), y/float(model.size), crab[y][x])
#        ax.text(y/float(model.size), 1, x/float(model.size), lotus[y][x])

length1 = 0
length2 = 0
length3 = 0
length4 = 0

for i in range(len(model.lxss)):
    #if model.lzss[i][0] == 1:
    ax.plot(model.lxss[i], model.lzss[i], zs=model.lyss[i], lw=5)

for m in model.modeldata:
    if m['length'] == 1:
        length1 += 1
    elif m['length'] == 2:
        length2 += 1
    elif m['length'] == 3:
        length3 += 1

#for point in model.fixed_points:
#    print(model.is_deletable(point[0], point[1], point[2]))

print("Analytics：\n* 10cm:" + str(length1) + "\n* 20cm:" + str(length2) + " \n* 30cm:" + str(length3))
print("Total: " + str(len(model.modeldata)))

print("\nSaving data files……")
f = open("modeldata.py", "w")
f2 = open(PATH_TO_MAYA_SCRIPT, "w")
f.write("modeldata=" + repr(model.modeldata))
f2.write(\
"""from maya.cmds import *
from maya.mel import eval

modeldata=""" + repr(model.modeldata) + \
"""\npipes = []

for m in modeldata:
    pipes.append(polyPipe(radius=3, height = m['length']*15))
    move(m['start'][0]*10-100, m['start'][1]*10-100, m['start'][2]*10-100)

select(*pipes)
polyUnite()
rotate(180, 0, 0)

eval("file -force -options \\"groups=1;ptgroups=1;materials=1;smoothing=1;normals=1\\" -typ \\"OBJexport\\" -pr -es \\"/Users/Sean/Desktop/Generative/模型/model.obj\\";")""")
f.close()
f2.close()



#ax.scatter(model.xs, model.zs, model.ys, c='g', marker='o')

#ax.set_xlabel('X Label')
#ax.set_ylabel('Y Label')
#ax.set_zlabel('Z Label')
print("Rendering 3D preview……")
plt.show()
