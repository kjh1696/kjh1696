number = int(input())

cnt = 1
for i in range(1,11):
    cnt = cnt * i
    if cnt >= number:
        print(f"{i}")
        break