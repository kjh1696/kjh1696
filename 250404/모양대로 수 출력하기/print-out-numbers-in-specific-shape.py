n = int(input())
cnt = n

for i in range(n): 

    for j in range(0,i):
        print(f" ", end = " ")

    for k in range(cnt,0,-1):
        print(f"{k}", end = " ")
    cnt = cnt -1

        
    print()