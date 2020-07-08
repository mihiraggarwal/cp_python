# https://www.hackerrank.com/challenges/word-order/problem

import sys
dictt = {}
for i in a[1:]:
    if i in dictt.keys():
        dictt[i] += 1
    else:
        dictt[i] = 1
print(len(dictt.items()))
for i in dictt.values():
    print(i, end = ' ')
