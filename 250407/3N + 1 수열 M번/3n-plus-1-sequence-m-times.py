n = int(input())

for _ in range(n):
    arr = input().split()
    a = int(arr[0])

    count = 0

    while a != 1:
        if a % 2 != 0:
            a = a * 3 + 1
            count = count + 1
        else:
            a = a /2
            count = count + 1

    print(f"{count}") 
