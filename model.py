

class Model:

    def __init__(self, size, graph1, graph2):
        self.size = size
        self.lines = 0
        self.matrix = [[[0 for i in range(size)] for j in range(size)] for k in range(size)]
        self.final_matrix = [[[0 for i in range(size)] for j in range(size)] for k in range(size)]
        self.xygraph = graph1
        self.zygraph = graph2
        self.xs = []
        self.ys = []
        self.zs = []

        self.modeldata = []

        self.lxss = []
        self.lyss = []
        self.lzss = []

        print("* 生成投影交点……", end='')

        #calculate fixed points
        self.fixed_points = []
        for y in range(self.size):
            for x in range(self.size):
                if self.xygraph[y][x] == 1:
                    for z in range(self.size):
                        if self.zygraph[y][z] == 1:
                            self.fixed_points.append((x, y, z))
                            self.matrix[x][y][z] = 1
                            self.xs.append(x)
                            self.ys.append(y)
                            self.zs.append(z)

        #generate initial tubes

        def is_deletable(x, y, z):
            if x <= 10:
                for tmpx in range(0, x):
                    if self.matrix[tmpx][y][z] == 1:
                        if y <= 10:
                            for tmpy in range(0, y):
                                if self.matrix[x][tmpy][z] == 1:
                                    return True
                        else:
                            for tmpy in range(y+1, 21):
                                if self.matrix[x][tmpy][z] == 1:
                                    return True
            else:
                for tmpx in range(x+1, 21):
                    if self.matrix[tmpx][y][z] == 1:
                        if y <= 10:
                            for tmpy in range(0, y):
                                if self.matrix[x][tmpy][z] == 1:
                                    return True
                        else:
                            for tmpy in range(y+1, 21):
                                if self.matrix[x][tmpy][z] == 1:
                                    return True
            return False
            
        print("完成\n* 优化节点数量……", end='')
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    if self.matrix[x][y][z] == 1:
                        if not is_deletable(x, y, z):
                            self.final_matrix[x][y][z] = 1

        start = 0
        print("完成\n* 数据格式化……", end='')
        for x in range(self.size):
            for z in range(self.size):
                started = False;
                for y in range(self.size):
                    length = 1;
                    if self.final_matrix[x][y][z] == 1:
                        if started == True:
                            length += 1
                        else:
                            start = y
                            started = True
                            length = 1
                    else:
                        if started:
                            started = False
                            self.lxss.append([x, x])
                            self.lyss.append([start-0.5, y-0.5])
                            self.lzss.append([z, z])
                            self.lines += 1
                            self.modeldata.append({
                                "start": (x, start-0.5, z),
                                "length": y - start
                            })
        print("完成\n\n")


    def is_deletable(self, x, y, z):
        if x <= 10:
            for tmpx in range(0, x):
                if self.matrix[tmpx][y][z] == 1:
                    if y <= 10:
                        for tmpy in range(0, y):
                            if self.matrix[x][tmpy][z] == 1:
                                return True
                    else:
                        for tmpy in range(y+1, 21):
                            if self.matrix[x][tmpy][z] == 1:
                                return True
        else:
            for tmpx in range(x+1, 21):
                if self.matrix[tmpx][y][z] == 1:
                    if y <= 10:
                        for tmpy in range(0, y):
                            if self.matrix[x][tmpy][z] == 1:
                                return True
                    else:
                        for tmpy in range(y+1, 21):
                            if self.matrix[x][tmpy][z] == 1:
                                return True
        return False










    #def step():
