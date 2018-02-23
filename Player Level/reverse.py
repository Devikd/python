num=int(input("Enter the number to be reversed:"))
r=0
while(num>0):
    digit=num%5
    r=r*5+digit
    num=num//5
print("Reverse of the given number:",r)
