Price,Avaseats,T,Hiked,x=map(int,input().split())
sum=0
for i in range(x):
    if(Avaseats>T):
        sum=sum+Price
        Avaseats=Avaseats-1
        x=x-1
    else:
        sum=sum+Hiked
        Avaseats=Avaseats-1
        x=x-1
print(sum)