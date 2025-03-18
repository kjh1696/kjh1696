numbers = int(input())

i = 1
cnt = 0
while i < numbers:
    if numbers%i == 0:
        cnt = cnt + i
    i = i + 1

if (cnt == numbers):
    print(f"P")
else:
    print(f"N")
