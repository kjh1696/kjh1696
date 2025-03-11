numbers = input()
numbers = numbers.split(" ")
A = int(numbers[0])
B = int(numbers[1])

for i in range(A, B+1):
    if i % 2 != 0:
        print(f"{i}", end = ' ')