n=int(input())
a=list(map(int,input().split()))
r=set()
d=[]
for num in a:
    if num not in r:
        r.add(num)
        d.append(num)
print(" ".join(map(str,d)))
