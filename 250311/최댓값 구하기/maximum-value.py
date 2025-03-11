numbers = input()
numbers = numbers.split(" ")
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

if a >= b and a >= c:
    print(f"{a}")

elif b >= a and b >= c:
    print(f"{b}")

elif c >= b and c >= a:
    print(f"{c}")