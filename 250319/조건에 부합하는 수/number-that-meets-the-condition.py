A = int(input())

for i in range(1,A+1,1):
    if (i % 2 == 0 and i % 4 != 0):
        continue
    if ((i//8)%2 == 0):
        continue
    if ((i%7) < 4):
        continue
    
    print(f"{i}", end = ' ')