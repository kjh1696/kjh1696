arr = list(map(int, input().split()))

n = len(arr)

sum_val = 0
for i in range(1, n, 2):
    sum_val += arr[i]

sum_vall = 0
for i in range(2,n,3):
    sum_vall += arr[i]

print(f"{sum_val} {sum_vall/3:0.1f}", end =" ")