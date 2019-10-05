N = int(input())
for i in range(N):
    words = [list(i) for i in input().split()]
    if sorted(words[0]) == sorted(words[1]):
        print("YES")
    else:
        print("NO")