p1 = input()
p1 = p1.split(" ")

age1 = int(p1[0])
sex1 = str(p1[1])

p2 = input()
p2 = p2.split(" ")

age2 = int(p2[0])
sex2 = str(p2[1])

if (age1 >= 19 and sex1 == "M") or (age2 >= 19 and sex2 == "M"):
    print(f"1")
else:
    print(f"0")