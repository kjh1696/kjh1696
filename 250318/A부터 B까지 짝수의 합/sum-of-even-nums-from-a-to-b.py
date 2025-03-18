numbers = input()
numbers = numbers.split(" ")

A = int(numbers[0])
B = int(numbers[1])

cnt = 0
while A < (B+1):
    if A%2 == 0:
        cnt = cnt + A
    A = A+1

print(f"{cnt}")