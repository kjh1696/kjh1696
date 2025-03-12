numbers = input()
numbers = numbers.split()

B = int(numbers[0])
A = int(numbers[1])

while A <= B:
    if B%2 == 0:
        print(f"{B}", end = ' ')
    B = B-1