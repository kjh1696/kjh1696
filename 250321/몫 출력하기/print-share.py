
count = 0
while True:
    number = int(input())

    if number % 2 == 1:
        continue
    elif number % 2 == 0:
        print(f"{number // 2}")
        count = count + 1

    if count == 3:
        break