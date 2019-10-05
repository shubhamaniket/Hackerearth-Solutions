n=int(input())
m=list(map(int,input().split()))
search=int(input())
for i in m:
    if(i==search):
        print(m.index(i))