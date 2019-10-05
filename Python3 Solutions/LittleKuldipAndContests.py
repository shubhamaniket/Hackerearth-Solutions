n=int(input())
found=False
for i in range(n):
    time=input()
    minutes1=time[3:4]
    m1=int(minutes1)
    minutes2=time[9:11]
    m2=int(minutes2)
    if m1<m2:
        found=True
if found:
    print("Will need a moderator!")
else:
    print("Who needs a moderator?")