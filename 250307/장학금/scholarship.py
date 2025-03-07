scores = input()
scores = scores.split()

score1 = int(scores[0])
score2 = int(scores[1])

if score1 >= 90:
    if score2 >= 95:
        print(f"100000")
    elif score2 >= 90:
        print(f"50000")
    else:
        print(f"0")
else:
    print(f"0")