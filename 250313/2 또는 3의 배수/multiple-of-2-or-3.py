N = input()
N = int(N)

for i in range(1,N+1):
    if i%2 == 0 or i %3 == 0:
        print(f"1", end = ' ')
    else:
        print(f"0", end = ' ')