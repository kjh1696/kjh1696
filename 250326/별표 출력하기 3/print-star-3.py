n = int(input())

for j in range(n,0,-1):
    for i in range(n-j):
        print(f"  ", end = "")
    
    for i in range(1,2 * j):
        print(f"* ", end = "")
    
    print()