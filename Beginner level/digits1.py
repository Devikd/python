x=int(input())
g=0
while(x!=0):
  d=x%10
  g=g+d**2
  x=x//10
print(g)
