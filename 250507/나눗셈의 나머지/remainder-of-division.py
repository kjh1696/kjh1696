arr = list(map(int, input().split()))
A = arr[0]
B = arr[1]

num = [0] * A
while A > 1:
    num[A%B] = num[A%B] + 1
    A = int(A / B)


sum = 0
for i in range (len(num)):
    if num[i] != 0:
        sum = sum + num[i]**2;

print(f"{sum}")
