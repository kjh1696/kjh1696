count = int(input())

cnt = 0
for i in range (count):
    number = int(input())
    if (number % 2 != 0 and number % 3 ==0):
        cnt = cnt + number

print(f"{cnt}")