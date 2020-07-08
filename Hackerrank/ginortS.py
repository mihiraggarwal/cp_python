# https://www.hackerrank.com/challenges/ginorts/problem

a = input()
b = sorted([i for i in a])
low, high, odd, even = [], [], [], []
for i in b:
    try:
        i = int(i)
        if i%2!=0:
            odd.append(i)
        else:
            even.append(i)
    except:
        if i == i.lower():
            low.append(i)
        elif i == i.upper():
            high.append(i)
final = sorted(low) + sorted(high) + sorted(odd) + sorted(even)
for i in final:
    print(i, end='')
