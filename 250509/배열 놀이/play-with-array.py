arr_first = list(map(int, input().split()))
arr_second = list(map(int, input().split()))

for i in range(arr_first[0]):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        if 1 <= arr[1] <= len(arr_second):
            print(f"{arr_second[arr[1]-1]}")
        else:
            print("Invalid index")

    elif arr[0] == 2:
        for j in range(len(arr_second)):
            if arr[1] == arr_second[j]:
                print(f"{j+1}")
                break
        else:
            print(f"0")

    elif arr[0] == 3:
        start = max(arr[1] - 1, 0)
        end = min(arr[2], len(arr_second))
        for k in range(start, end):
            print(f"{arr_second[k]}", end=" ")
        print()
