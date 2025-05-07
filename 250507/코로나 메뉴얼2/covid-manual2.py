step = [0,0,0,0]

for i in range(0,3):
    s = input()
    parts = s.split()

    letter = parts[0]
    number = int(parts[1])

    if letter == "Y" and number >= 37:
        step[0] = step[0] + 1
    elif letter == "N" and number >= 37:
        step[1] = step[1] + 1
    elif letter == "Y" and number < 37:
        step[2] = step[2] + 1
    else:
        step[3] = step[3] + 1

for i in range(0,4):
    print(f"{step[i]}", end = " ")

if step[0] >= 2:
    print(f"E")