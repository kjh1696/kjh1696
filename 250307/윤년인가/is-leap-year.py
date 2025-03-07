Y = int(input())

if Y%100 == 0 and Y%400 != 0:
    print(f"false")
elif Y%4 == 0:
    print(f"true")
else:
    print(f"false")