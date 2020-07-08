# https://www.hackerrank.com/challenges/no-idea/problem

import sys
inp = [i for i in sys.stdin.read().split('\n')]
numbers = [int(i) for i in inp[0].split()]
array = [int(i) for i in inp[1].split()]
a = [int(i) for i in inp[2].split()]
b = [int(i) for i in inp[3].split()]
final = 0
for i in array:
    if i in a : final += 1
    elif i in b : final -= 1
    else : continue
sys.stdout.write(f'{final}\n')
