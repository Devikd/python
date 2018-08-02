g,d=input().split()
d=int(d)
l=[int(x) for x in input().split()]
l1=[int(x) for x in input().split()]
for x in l1:
    l.append(x)
for i in range(d):
    print (max(l))
    l.remove(max(l))
