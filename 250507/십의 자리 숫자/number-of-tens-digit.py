arr = list(map(int, input().split()))

num = [0,0,0,0,0,0,0,0,0,0]

for j in range(len(arr)):
    if arr[j] == 0:
        break
    else:
        num[int(arr[j]/10)] = num[int(arr[j]/10)] + 1

for i in range(1,10):
    print(f"{i} - {num[i]}", end = "\n")