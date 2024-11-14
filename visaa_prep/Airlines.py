x,y=map(int,input().split())
cap=x*100
if y>cap:
    new_cap=(y-cap+99)//100
    print(new_cap)
else:
    print("0")
