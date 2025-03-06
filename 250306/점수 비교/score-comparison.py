A_math_english = input()
A_math_english = A_math_english.split(" ")

A_math = int(A_math_english[0])
A_english = int(A_math_english[1])

B_math_english = input()
B_math_english = B_math_english.split(" ")

B_math = int(B_math_english[0])
B_english = int(B_math_english[1])

if A_math > B_math and A_english > B_english:
    print(f"1")
else:
    print(f"0")