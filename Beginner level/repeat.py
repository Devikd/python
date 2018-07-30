asc = 256
def rep(str):
    g = [0] * asc
    max = -1
    d = ''
    for i in str:
        g[ord(i)]+=1;
    for i in str:
        if max < g[ord(i)]:
            max = g[ord(i)]
            d = i
    return d
str = input()
print(rep(str))
