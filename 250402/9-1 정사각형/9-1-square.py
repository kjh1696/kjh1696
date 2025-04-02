n = int(input())

cnt = 9
for i in range(n,0,-1): 
    for j in range(n):
        print(f"{cnt}" , end="")
        cnt -= 1

        if cnt == 0:
            cnt = 9
    print()