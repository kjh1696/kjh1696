numbers = input()
numbers = numbers.split()

num1 = int(numbers[0])
num2 = int(numbers[1])

num = num1

while num <= num2:
    if num%2 != 0:
        print(f"{num}", end = " ")
        num = num*2
       
    else:
        print(f"{num}", end = " ")
        num = num + 3
