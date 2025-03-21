while True:
    numbers = input()
    numbers = numbers.split(" ")
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    alphabet =  numbers[2]

    print(f"{num1 * num2}")

    if alphabet == 'C':
        break
