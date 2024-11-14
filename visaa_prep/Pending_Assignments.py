x,y,z=map(int,input().split())
tt=x*y
at=z*60*24
if tt<=at:
    print("YES")
else:
    print("NO")
