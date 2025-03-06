numbers = input()
numbers = numbers.split(" ")

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

if a <= b and a <= c:
    min = a
elif b <= c and b <= a:
    min = b
elif c <= a and c <= b:
    min = c

print(f"{min}")