inputs = input()
inputs = inputs.split(" ")

a = int(inputs[0])
b = int(inputs[1])

if a < b:   
    a1 = ("1")
elif a >= b:
    a1 = ("0")

if a==b:
    b1 = ("1")
else:
    b1 = ("0")


print(f"{a1} {b1}")