num = list(map(int, input().split()))
arr = []

arr.append(num[0])
arr.append(num[1])

for i in range(10):
    arr.append((arr[i] + arr[i+1])%10)

print(*arr[0:10]) 
