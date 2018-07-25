d=input()
g=len(d)
while True:
    if " " in d:
        g=g-1
        if(" " not in d):
          break
        print(g)
        break
    else:
        print(g)
        break 
