numbers = input()
numbers = numbers.split()

num1 = int(numbers[0])
num2 = int(numbers[1])


for i in range(2, 10, 2 ): 
    count = 1 
    for j in range(num2, num1 -1, -1):

        if count == 1:
            print(f"{j} * {i} = {i * j}", end=" ")
            count = count + 1

        elif count != 1:
            print(f"/ {j} * {i} = {i * j}", end=" ")
    print()