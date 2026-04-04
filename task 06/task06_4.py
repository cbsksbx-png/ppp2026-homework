from cmath import cos
from math import degrees, radians

import math
for i in range(0 , 90 + 1) :
    rad = math.radians(i)
    sin = round(math.sin(rad), 4)
    cos = round(math.cos(rad), 4)
    tan = round(math.tan(rad), 4)
    print(f"{round(rad, 4)}, {sin}, {cos}, {tan}")
