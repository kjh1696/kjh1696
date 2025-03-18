numbers = input()
numbers = numbers.split(" ")

A = int(numbers[0])
B = int(numbers[1])

cnt = 0
if B > A:
    while A < (B+1):
        if A% 5 == 0:
            cnt = cnt + A
        A = A + 1
elif B <= A:
    while B < (A+1):
        if B % 5 == 0 :
            cnt = cnt + B
        B = B + 1

print(f"{cnt}")
            
