numbers = input()
numbers = numbers.split()

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

if a%c > 0:
    print(f"YES")
else:
    print(f"NO")