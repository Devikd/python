d=int(input())
a=[]
for i in range(0,d):
    g=int(input())
    a.append(g)
count=0
for i in a:
    for x in a:
        if i==x:
            count+=2
    if count==2:
         print(i)
