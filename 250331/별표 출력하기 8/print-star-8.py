n = int(input())

for i in range(1,n+1):
    if i%2 != 0:
        print(f"*", end = "")
        print()
    else:
        for j in range(i):
            print(f"* ",end = "")
        print()