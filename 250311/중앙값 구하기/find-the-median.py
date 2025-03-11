numbers = input()
numbers = numbers.split(" ")

f = int(numbers[0])
s = int(numbers[1])
t = int(numbers[2])

if (f >= s and f <= t) or (f >= t and f <= s):
    print(f"{f}")
elif (s >= f and s <= t) or (s >= t and s <= f):
    print(f"{s}")
elif (t >= f and t <= s) or (t >= s and t <= f):
    print(f"{t}")

