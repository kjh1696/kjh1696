count = 0
cnt = 0
for i in range(10):
    numbers = int(input())
    if (numbers >=0 and numbers <= 200):
        cnt = cnt + numbers
        count = count + 1

print(f"{cnt} {cnt/count:.1f}")
