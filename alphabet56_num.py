n=input("Enter Alphanumeric")
v=0
g=0
for char in n:
    if(char.isdigit()):v=v+1
    if(char.isalpha()):g=g+1
    if(v>0 and g>0):
        print('yes')
        break
if(v==0 or g==0):print('No')
