n=int(input())
a=list(map(int,input().split()))
mc=0
ca=0
for d in a:
    if d==0:
        ca+=1
        mc=max(mc,ca)
    else:
        ca=0
print(mc)
