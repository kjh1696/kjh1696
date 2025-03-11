first_people = input()
first_people = first_people.split(" ")
p1_cold = first_people[0]
p1_temp = int(first_people[1])

second_people = input()
second_people = second_people.split(" ")
p2_cold = second_people[0]
p2_temp = int(second_people[1])

third_people = input()
third_people = third_people.split(" ")
p3_cold = third_people[0]
p3_temp = int(third_people[1])

A = 0

if p1_cold == "Y" and p1_temp >= 37:
    A = A+1

if p2_cold == "Y" and p2_temp >= 37:
    A = A+1

if p3_cold == "Y" and p3_temp >= 37:
    A = A+1

if A >= 2:
    print(f"E")
else:
    print(f"N")