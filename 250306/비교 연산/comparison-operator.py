numbers = input()
numbers = numbers.split()

num1 = int(numbers[0])
num2 = int(numbers[1])

print(int(num1 >= num2))
print(int(num1 > num2))
print(int(num2 >= num1))
print(int(num2 > num1))
print(int(num1 == num2))
print(int(num1 != num2))