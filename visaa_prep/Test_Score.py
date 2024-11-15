x,y,z=map(int,input().split())
if z%y==0 and z<=x*y:
    print("YES")
else:
    print("NO")
