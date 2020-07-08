# https://www.hackerrank.com/challenges/triangle-quest-2/problem

for i in range(1,int(input())+1):
    print((sum(list(map(lambda i:10**(i-1), list(range(1, i+1))))))**2)
