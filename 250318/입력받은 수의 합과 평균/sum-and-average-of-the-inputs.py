integer = int(input())

cnt = 0
for i in range(integer):
    numbers = int(input())
    cnt = cnt + numbers

print(f"{cnt} {cnt/integer:.1f}")
