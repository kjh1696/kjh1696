arr = list(map(int, input().split()))

num = [0,0,0,0,0,0,0,0,0,0,0]

for j in range(len(arr)):
    if arr[j] == 0:
        break
    else:
        num[int(arr[j]/10)] = num[int(arr[j]/10)] + 1

for i in range(10 , 0 , -1):
    print(f"{i * 10} - {num[i]}", end = "\n")