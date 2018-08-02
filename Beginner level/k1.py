p=int(input())
l=int(input())
if(p<=100000 & l<=100000):
  while(p!=l):
    if(p>l):
      p-=l
    else:
      l-=p
  print(p)
