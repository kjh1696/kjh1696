A_student = input()
B_student = input()

A_student = A_student.split()
B_student = B_student.split()

A_math = A_student[0]
A_eng = A_student[1]

B_math = B_student[0]
B_eng = B_student[1]

if A_math > B_math:
    print("A")
elif B_math > A_math:
    print("B")
else:
    if A_eng > B_eng:
        print(f"A")
    else:
        print(f"B")