prod = 1
numbers = input()
numbers = numbers.split(" ")

A = int(numbers[0])
B = int(numbers[1])

while A <= B:
    prod = prod * A
    A = A+1

print(f"{prod}")