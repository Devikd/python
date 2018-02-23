num1=int(input("enter lower limit"))
num2=int(input("enter upper limit"))
a = []
for i in range(num1, num2+1):
    for j in range(i*i, num2+1, i):
            a.append(j)
    if i not in a:
            print (i)
