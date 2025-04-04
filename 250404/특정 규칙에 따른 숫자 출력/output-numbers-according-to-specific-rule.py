n = int(input())
cnt = n
count = 1

for i in range(n): 

    for j in range(0,i):
        print(f" ", end = " ")

    for k in range(cnt,0,-1):
        print(f"{count}", end = " ")
        count = count +1

        if count == 10:
            count = 1

    cnt = cnt - 1

        
    print()