numbers = input()
numbers = numbers.split()

A = int(numbers[0])
B = int(numbers[1])

if A > 0:
    for i in range(1,B+1):
        print(f"{A}", end = '')
else:
    print(f"0")