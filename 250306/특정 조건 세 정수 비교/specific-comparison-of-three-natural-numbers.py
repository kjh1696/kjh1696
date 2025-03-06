numbers = input()
numbers = numbers.split()

num1 = int(numbers[0])
num2 = int(numbers[1])
num3 = int(numbers[2])

if num1 <= num2 and num1 <= num3:
    min = num1
elif num2 <= num1 and num2 <= num3:
    min = num2
elif num3 <= num1 and num3 <= num2:
    min = num3

if(num1 == min):
    ans1 = "1"
else:
    ans1 =  "0"

if num1 == num2 and num2 == num3:
    ans2 = "1"
else:
    ans2 = "0"

print(f"{ans1} {ans2}")
