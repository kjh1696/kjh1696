n = int(input())

cnt = 1
for i in range(n): 
    for j in range(n):
        print(f"{cnt*2} " , end="")
        cnt += 1

        if cnt*2 == 10:
            cnt = 1
    print()