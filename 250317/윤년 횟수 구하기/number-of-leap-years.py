numbers = int(input())

cnt = 0
for i in range (numbers+1):
    if i == 0:
        continue
    elif (i % 100 == 0 and i % 400 != 0):
        continue
    elif (i % 4 == 0):
        cnt = cnt + 1

print(f"{cnt}")