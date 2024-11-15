m=int(input())
if m<1 or m>12:
    print("Invalid")
elif 3<=m<=5:
    print("Spring")
elif 6<=m<=8:
    print("Summer")
elif 9<=m<=11:
    print("Autumn")
else:
    print("Winter")
