import statistics
x=list()
nu=input()
for i in range(int(nu)):
  n=input()
  x.append(int(n))
print(x)
x.sort()
print(x)
print(statistics.median(x))
