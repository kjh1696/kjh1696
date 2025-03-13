numbers = input()
numbers = numbers.split()

A = int(numbers[0])
B = int(numbers[1])

for i in range(B):
    A = A + B
    print(f"{A}")