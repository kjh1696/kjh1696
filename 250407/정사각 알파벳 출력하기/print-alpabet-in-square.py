n = int(input())
cnt = 0

for i in range(n):
    for j in range(n):
        print(f"{chr(65 + cnt)}", end = "")
        cnt = cnt + 1
    print()
