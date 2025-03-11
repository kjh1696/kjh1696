numbers = input()
numbers = numbers.split()

B = int(numbers[0])
A = int(numbers[1])

for i in range(B, A-1, -1):
    if i % 2 == 1:
        print(f"{i}", end = ' ')