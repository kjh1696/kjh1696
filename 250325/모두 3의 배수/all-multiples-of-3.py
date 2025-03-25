count = 0
for i in range(1,6):
    number = int(input())
    if number % 3 == 0:
        count = count + 1

if count == 5:
    print(f"1")
else:
    print(f"0")