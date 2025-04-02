numbers = input()
numbers = numbers.split()

i = int(numbers[0])
j = int(numbers[1])

for i in range(1, i+1): 
    for j in range(1, j+1):
        print(f"{i * j} " , end="")
    print()