t=int(input())
l=[]
res=[]
for i in range(0,t):
    num=int(input())
    l.append(num)
for j in l:
    count=0
    i=5
    while (j / i >= 1):
        count += int(j / i)
        i *= 5
    res.append(count)
for i in res:
    print(i)
