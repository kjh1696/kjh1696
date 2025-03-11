numbers = input()
numbers = numbers.split(" ")

f = int(numbers[0])
s = int(numbers[1])
t = int(numbers[2])

if (f >= s and f <= t) or (f >= t and f <= s):
    print(f"{f}")

if (s >= f and s <= t) or (s >= f and s <= t):
    print(f"{s}")

if (t >= f and t <= s) or (t >= f and t <= s):
    print(f"{t}")