sex = int(input())
year = int(input())

if sex == 0:
    if year >= 19:
        print(f"MAN")
    else:
        print(f"BOY")

else:
    if year >= 19:
        print(f"WOMAN")
    else:
        print(f"GIRL")