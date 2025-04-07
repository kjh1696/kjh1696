n = int(input())
cnt = 0

for i in range(n,0,-1):

    for k in range(n-i):
        print(f" ", end = " ")
      
    for l in range(i):
        print(f"{chr(65 + cnt)}", end = " ")
        cnt = cnt+1

        if cnt >= 26:
            cnt = 0

    print()
