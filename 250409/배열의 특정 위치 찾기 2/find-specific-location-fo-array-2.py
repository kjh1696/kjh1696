arr = list(map(int, input().split()))

sum_even = []
sum_odd = []

for i in range(len(arr)):
    if i % 2 == 0:
        sum_even.append(arr[i])
    else:
        sum_odd.append(arr[i])

print(f"{abs(sum(sum_even) - sum(sum_odd))}", end = "")

