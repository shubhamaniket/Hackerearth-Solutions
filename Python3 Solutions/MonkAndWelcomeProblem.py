N=int(input(""))
num_1=list(map(int,input("").split()))
num_2=list(map(int,input("").split()))
sum_array=[]
for i in range(N):
    sum_1=(num_1[i]+num_2[i])
    sum_array.append(sum_1)
for element in sum_array:
    print(element,end=" ")
print("")