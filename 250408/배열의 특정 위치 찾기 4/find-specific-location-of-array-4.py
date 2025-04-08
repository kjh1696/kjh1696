my_arr = list(map(float, input().split()))
arr = []

count = 0
for i in range(10):
    if my_arr[i] == 0:
        break

    elif my_arr[i] % 2 == 0:
        arr.append(my_arr[i])
        count = count + 1


print(f"{count:.0f} {sum(arr):.0f}", end = " ")