a=int(input('Enter a number '))
b=len(str(a))
d=[]
while b!=0:
    for number in range(0, b):
        c=str(a)[number]
        c=int(c)
        d.append(c)
    e=sum(d)
    print(e)
    a=e
    b=len(str(e))
    d.clear()
    if b==1:
        break

