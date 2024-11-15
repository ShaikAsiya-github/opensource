def ri(n):
    INT_MIN,INT_MAX=-2**31,2**31-1
    s=-1 if n< 0 else 1
    rn=int(str(abs(n))[::-1])*s
    if rn < INT_MIN or rn > INT_MAX:
        return 0
    return rn
n=int(input())
print(ri(n))
