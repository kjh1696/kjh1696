number = int(input())

for i in range(2,number):
    if number % i == 0:
        print(f"C")
        break

if i == (number-1):
    print(f"P")