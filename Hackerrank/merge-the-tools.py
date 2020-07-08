# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    length = len(string)
    first = []
    final = []
    a=set()
    c=''
    for i in range(0, length, k):
        first.append(string[i:i+k])
    for i in first:
        for j in i:
            a.add(j)
        for k in a:
            c+=k
        final.append(c)
        c=''
        a=set()
    for i in final : print(i)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
