n = int(input())

for i in range(0,2*n+1): 
    for j in range(0,2*n+1):
        if i == 0 or i % 2 == 0  or j == 0 or j % 2 == 0:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
