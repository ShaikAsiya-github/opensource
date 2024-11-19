n=int(input())
a=list(map(int,input().split()))
rarr=a[1:]+a[:1]
print(" ".join(map(str,rarr)))
