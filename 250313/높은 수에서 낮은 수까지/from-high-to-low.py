numbers = input()
numbers = numbers.split()

A = int(numbers[0])
B = int(numbers[1])

if A >= B:
    for i in range(A,B-1, -1):
        print(f"{i}", end = ' ')
else:
    for i in range(B,A-1, -1): 
        print(f"{i}", end = ' ')