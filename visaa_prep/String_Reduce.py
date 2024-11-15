s=input()
res=[]
cc=s[0]
c=1


for i in range(1,len(s)):
    if s[i]==cc:
        c+=1
    else:
        res.append(f"{cc}{c}")
        cc=s[i]
        c=1
res.append(f"{cc}{c}")
print("".join(res))
