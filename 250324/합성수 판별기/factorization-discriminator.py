n = int(input())

for i in range(2,n):
    if n % i == 0:
        print(f"C")
        break

if i == (n-1):
    print(f"N")
