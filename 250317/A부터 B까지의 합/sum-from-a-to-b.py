sum_val = 0

numbers = input()
numbers = numbers.split()

num1 = int(numbers[0])
num2 = int(numbers[1])

while num1 <= num2:
    sum_val = sum_val + num1
    num1 = num1 + 1

print(f"{sum_val}")