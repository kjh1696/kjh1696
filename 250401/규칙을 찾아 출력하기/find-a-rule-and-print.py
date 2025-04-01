n = int(input())


for i in range(n): 
    for j in range(n):

        if i == 0 or j == n-1:
            print(f"* ", end="")
        
        elif i < n and i > j:
            print(f"* ", end="")
        
        else:
            print(f"  ", end = "")

    print()
