n = int(input())
cnt = n
count = 1

for i in range(1,n+1): 

    for j in range(0,i):
        print(f"{cnt + j} ", end = " ")
    
    cnt = cnt -1

    print()

        
