numbers = input()
numbers = numbers.split(" ")

num1 = int(numbers[0])
num2 = int(numbers[1])

count = 0
cnt = 0
while num1 < (num2+1):
    if(num1 % 5 == 0) or (num1 % 7 ==0):
        count = count + 1
        cnt = cnt + num1
    num1 = num1 + 1

print(f"{cnt} {cnt/count:.1f}")