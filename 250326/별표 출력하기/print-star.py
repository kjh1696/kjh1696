N = int(input())

for i in range(1,N+1,1):
    print(f"* "*i, end = "")
    print()

for i in range(N-1,0,-1):
    print(f"* "*i, end = "")
    print()