age = 0
count = 0
while True:
    number = int(input())

    if number > 29 or number < 20:
        print(f"{(age / count):.2f}")
        break

    else:
        age = age + number
        count = count + 1
    