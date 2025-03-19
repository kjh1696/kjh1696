N = int(input())

cnt = 0
for i in range(N):
    if (i+1) % 2 == 0:
        cnt = cnt + 1
        continue
    elif (i+1) % 3 == 0 :
        cnt = cnt + 1
        continue
    elif (i+1) % 5 == 0 :
        cnt = cnt + 1
        continue

print(f"{(N) - cnt}")