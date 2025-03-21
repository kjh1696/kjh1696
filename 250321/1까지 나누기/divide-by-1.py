N = int(input())

i = 1
count = 1
while (N//i) > 1:
    count = count + 1
    N = (N//i)
    i = i + 1


print(f"{count}")