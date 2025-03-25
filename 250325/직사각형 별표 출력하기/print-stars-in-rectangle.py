numbers = input()
numbers = numbers.split()

N = int(numbers[0])
M = int(numbers[1])

for i in range(1,N+1):
    for j in range(1, M+1):
        print(f"*", end = " ")
    print()