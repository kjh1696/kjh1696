arr_first = list(map(int, input().split()))
arr_second = list(map(int, input().split()))

for i in range(arr_first[1]):

    arr = input()
    arr = list(map(int, arr.split()))

    if arr[0] == 1:
        print(f"{arr_second[arr[1]-1]}")

    elif arr[0] == 2:
        for j in range(len(arr_second)):
            if arr[1] == arr_second[j]:
                print(f"{j+1}")
                break
        else:
            print(f"0")


    elif arr[0] == 3:
        for k in range(arr[1]-1 , arr[2]):
            print(f"{arr_second[k]}", end = " ")
        print()
