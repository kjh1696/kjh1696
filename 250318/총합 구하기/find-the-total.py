numbers = input()
numbers = numbers.split()

A = int(numbers[0])
B = int(numbers[1])

cnt = 0
while A <= B:
    if (A % 6 == 0 and A % 8 != 0):
        cnt = cnt + A
    A = A + 1

print(f"{cnt}")
    