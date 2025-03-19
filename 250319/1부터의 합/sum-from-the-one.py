N = int(input())

cnt = 0
for i in range(1, 100, 1):
    cnt = cnt + i
    if (cnt >= N):
        print(f"{i}")
        break

    