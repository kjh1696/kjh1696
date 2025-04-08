my_arr = list(map(float, input().split()))
arr = []

count = 0
for i in range(10):
    if my_arr[i] != 0:
        arr.append(my_arr[i])
        count = count + 1
    else:
        break


print(f"{sum(arr):.0f} {sum(arr)/count:.1f}", end = " ")