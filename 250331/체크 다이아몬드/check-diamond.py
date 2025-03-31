n = int(input())

count = 1
for i in range(n-1,-1,-1):

    for k in range (i):
        print(f" ", end = "")

    for j in range(count):
        print(f"* ", end = "")
    
    count = count + 1
    
    print()


for i in range (n-1,0,-1):

    for k in range(n-i):
        print(f" ", end = "")
    for j in range(i):
        print(f"* ", end = "")

    print()