days=int(input())
count=0
for i in range(days):
    r,x=map(int,input().split())
    perimeter=2*(22/7)*r
    x1=100*x
    if(perimeter<x1):
        count=count+1
print(count)