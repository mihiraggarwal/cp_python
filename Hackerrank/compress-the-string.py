# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby
s = input()
final = []
for i, j in groupby(s):
    final.append(len(list(j)))
    final.append(int(i))
    print(tuple(final), end=' ')
    final.clear()
