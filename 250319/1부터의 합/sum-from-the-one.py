N = int(input())

cnt = 0
for i in range(1, 100, 1):
    if (cnt >= N):
        print(f"{i-1}")
        break
    cnt = cnt + i 
    