v="hello world.123"
count=0
n=len(v)
for i in range(0,n):
    if(v[i]>='0' and v[i]<='9'):
        count=count+1
print(count)        
