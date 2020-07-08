# https://www.hackerrank.com/challenges/find-angle/problem

import math
a = int(input())
b = int(input())
ratio = a/b
print(round(math.degrees(math.atan(ratio))), end='')
print('°')
