p = int(input())
    
count = p

for i in range(1,p+1):
    count = count - 1

    for j in range (count):
        print(f" ", end = "")
    
    n = 2 * i -1
    for k in range (n):
        print(f"*", end = "")

    print()

for i in range(p-1,0,-1):
    count = count + 1

    for j in range(count):
        print(f" ", end = "")
    
    n = 2 * i - 1
    for k in range(n):
        print(f"*", end = "")
    
    print()