numbers = input()
numbers = numbers.split()

A = int(numbers[0])
B = int(numbers[1])

cnt = 1
for i in range(B):
    if ((i+1)%A == 0):
        cnt = cnt * (i+1)

print(f"{cnt}")

