numbers = input()
numbers = numbers.split()

A = int(numbers[0])
B = int(numbers[1])

while A <= B:
    if A%2 == 0:
        print(f"{A}", end = ' ')
    A = A+1