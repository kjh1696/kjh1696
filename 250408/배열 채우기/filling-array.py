my_arr = list(map(float, input().split()))
arr = []

for i in range(10):
    if my_arr[i] != 0:
        arr.append(my_arr[i])
    else:
        break


for i in range(len(arr)-1,-1,-1):
    print(f"{arr[i]:.0f}", end = " ")