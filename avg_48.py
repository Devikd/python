num2 = int(input())
list=[]
count=0
for i in range(0,num2):
    total=int(input())
    count+=total
    list.append(total)
print(int(count/num2))
