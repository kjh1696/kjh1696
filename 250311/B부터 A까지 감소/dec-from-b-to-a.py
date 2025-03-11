numbers = input()
numbers = numbers.split()

A = int(numbers[0])
B = int(numbers[1])

for i in range(B, A-1, -1):
    print(f"{i}", end = ' ')