g=[]
d=int(input("value"))
for i in range(1,d+1):
 n=int(input("numbers"))
 g.append(n)
 g.sort()
print(g)
print(g[d//2])
