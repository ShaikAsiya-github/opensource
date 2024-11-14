x,y,z=map(int,input().split())
rest=z-y
if rest<0:
    print("0")
else:
    print(rest//x)
