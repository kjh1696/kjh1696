numbers = input()
numbers = numbers.split()

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

for i in range(a,b+1):
    if i % c == 0:
        print(f"NO")
        break

if i == b:
    print(f"YES")