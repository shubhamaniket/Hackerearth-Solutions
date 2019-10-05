num=int(input())
count=0
count_1=0
count_2=0
count_3=0
count_4=0
count_5=0
count_6=0
count_7=0
count_8=0
count_9=0
while(num!=0):
    digit=num%10
    if(digit==0):
        count=count+1
    elif(digit == 1):
        count_1 = count_1 + 1
    elif(digit == 2):
        count_2 = count_2 + 1
    elif(digit == 3):
        count_3 = count_3 + 1
    elif(digit == 4):
        count_4 = count_4 + 1
    elif(digit == 5):
        count_5 = count_5 + 1
    elif(digit == 6):
        count_6 = count_6 + 1
    elif(digit == 7):
        count_7 = count_7 + 1
    elif(digit == 8):
        count_8 = count_8 + 1
    elif(digit == 9):
        count_9 = count_9 + 1
    num=num//10
print(0,count)
print(1,count_1)
print(2,count_2)
print(3,count_3)
print(4,count_4)
print(5,count_5)
print(6,count_6)
print(7,count_7)
print(8,count_8)
print(9,count_9)