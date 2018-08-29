nterms=int(input())
n11 = 0
n21 = 1
count = 0
while count < nterms:
    print(n11)
    nth = n21 + n21
    n11 = n21
    n21 = nth
    count += 1
