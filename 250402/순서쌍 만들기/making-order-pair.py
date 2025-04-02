n = int(input())

for i in range(n,0,-1): 
    for j in range(0,n):
        print(f"({i},{n-j}) ", end = "")
    print()
