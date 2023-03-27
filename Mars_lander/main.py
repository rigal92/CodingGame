import pandas as pd
import sys



# surface_n = int(input())  # the number of points used to draw the surface of Mars.
# surf = pd.DataFrame([[int(j) for j in input().split()] for i in range(surface_n)],columns = ["x","y"])
surface = [[0,100], [1000,500], [1500,1500], [3000,1000], [4000,150], [5500,150], [6999,800]]
surf = pd.DataFrame(surface,columns = ["x","y"])



print(surf.values,file=sys.stderr, flush = True)
# game loop
while True:

    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]



    print("-20 3")
