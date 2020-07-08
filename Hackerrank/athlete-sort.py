# https://www.hackerrank.com/challenges/python-sort-sort/problem

start = input().split(' ')
rows = []
for i in range(int(start[0])):
    a = list(map(int, input().split(' ')))
    rows.append(a)
k = int(input())
def index(ind):
    return ind[k]
rows.sort(key = index)
for i in rows:
    for j in i:
        print(j, end = ' ')
    print('')
