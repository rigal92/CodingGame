import pandas as pd
import sys

surface = [[0,100], [1000,500], [1500,1500], [3000,1000], [4000,150], [5500,150], [6999,800]]
surf = pd.DataFrame(surface,columns = ["x","y"])


# surface_n = int(input())  # the number of points used to draw the surface of Mars.
# surf = pd.DataFrame([[int(j) for j in input().split()] for i in range(surface_n)],columns = ["x","y"])

#find flat land
i = surf[surf.diff().y == 0].index.values
flat_m,flat_M = surf.loc[i.min()-1:i.max(), "x"]


# print(surf.values,file=sys.stderr, flush = True)
# game loop
while True:

    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    if x<flat_m or x>flat_M:

        if h_speed




    else:
        if h_speed != 0:
            a = int(45 * h_speed/abs(h_speed))
            p = 1
        else:
            a = 0
            p = 0




    print(f"{a} {p}")
