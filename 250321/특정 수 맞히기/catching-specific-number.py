while True:
    number = int(input())

    if number < 25:
        print(f"Higher")
    elif number > 25:
        print(f"Lower")
    elif number == 25:
        print(f"Good")
        break