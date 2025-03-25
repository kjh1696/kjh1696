N = int(input())

for j in range(N):
    for i in range(N-j, 0, -1):
        print(f"*", end = " ")
    print()
    
