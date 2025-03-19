N = int(input())

cnt = 0
for i in range(1, 101):
    cnt = cnt + i
    if (cnt >= N):
        print(f"{i}")
        break

    