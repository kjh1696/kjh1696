numbers = input()
numbers = numbers.split()

A = int(numbers[0])
B = int(numbers[1])

for i in range(A,B+1):
    if (1920 % i == 0 and 2880 % i == 0):
        print(f"1")
        break

if i == B:
    print(f"0")