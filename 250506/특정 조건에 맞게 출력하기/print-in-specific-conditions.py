
arr = list(map(int, input().split()))

i = 0
while arr[i] != 0:

    if arr[i] % 2 == 1:
        print(f"{int(arr[i] + 3)}", end= " ")
    else:
        print(f"{int(arr[i] / 2)}", end = " ")

    i = i + 1

