numbers = input()
numbers = numbers.split()

A = int(numbers[0])
B = int(numbers[1])

first = int(A/B)
divided = int((A%B)*10)
print(f"{first}.", end = '')

for i in range(20):
    share = int(divided/B)
    print(f"{share}", end = '')
    divided = int((divided % B) * 10)
