numbers = input()
numbers = numbers.split(" ")

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

if b > a and b < c:
    print(f"1")
else:
    print(f"0")