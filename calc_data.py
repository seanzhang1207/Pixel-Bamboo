#!/usr/local/bin/python3
#coding: utf-8

from model import Model
from graphs import crab, lotus

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

MODELSIZE = 21

fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(111, projection='3d')
#ax2 = fig.add_subplot(111, projection='3d')
print("设定图纸大小为 " + str(MODELSIZE) + "x" + str(MODELSIZE) + "，计算中")
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

print("统计数据：\n* 10cm:" + str(length1) + " 根\n* 20cm:" + str(length2) + " 根\n* 30cm:" + str(length3) + " 根")
print("共计 " + str(len(model.modeldata)) + " 根")

print("\n保存数据文件……")
f = open("modeldata.py", "w")
f2 = open("/Users/Sean/Library/Preferences/Autodesk/maya/2016/prefs/scriptEditorTemp/gen_model.py", "w")
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
print("显示效果图……")
plt.show()
