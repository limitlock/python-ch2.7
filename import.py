# 다양한 import 방법

# import math
# print(math.sin(math.pi/6), math.cos(math.pi/6))

# from math import pi, sin, cos
# from mymath import pi
# print(sin(pi/6), cos(pi/6))
# print(pi)

# from math import *
# import mymath as m
# print(sin(pi/6), cos(pi/6))
# print(m.pi)

from math import sin as mysin, cos as mycos
import mymath as m
print(mysin(m.pi/6), mycos(m.pi/6))
