a=int(input())
b=int(input())
c= [x for x in range(a,b) if int(x**0.5)==x**0.5]
print(int(len(c)),(""))
