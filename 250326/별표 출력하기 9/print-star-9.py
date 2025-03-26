n = int(input())

for j in range(0,n):
    for i in range(n-j-1):
        print(f"  ", end = "")
    
    for i in range(0,(2 * j+1)):
        print(f"* ", end = "")
    
    print()