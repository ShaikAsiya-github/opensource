x,y,z,s=map(int,input().split())
if (x+y>=s)or(y+z>=s)or(z+x>=s):
    print("YES")
else:
    print("NO")
