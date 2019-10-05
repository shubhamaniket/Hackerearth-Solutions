T=int(input())
for i in range(T):
    n=input()
    rev=n[::-1]
    if(rev==n and (len(n)%2==0)):
        print("YES EVEN")
    elif(rev==n and (len(n)%2!=0)):
        print("YES ODD")
    else:
        print("NO")