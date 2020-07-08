# https://www.hackerrank.com/challenges/python-quest-1/problem

for i in range(1, int(input())):
    print(i*(sum(list(map(lambda i:10**(i-1), list(range(1, i+1)))))))
