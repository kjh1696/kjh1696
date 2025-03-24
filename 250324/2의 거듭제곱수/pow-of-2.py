n = int(input())

count = 0
while n % 2 == 0:
    n = n // 2
    count = count + 1

print(f"{count}")