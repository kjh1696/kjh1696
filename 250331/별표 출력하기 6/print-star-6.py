n = int(input())

count = 0

p = n
n = 2 * n - 1

while n > 0:

    for i in range(0,count):
        print(f"  ", end = "")

    count = count + 1

    for i in range(0, n):
        print(f"* ", end = "")
    
    print()
    n = n - 2
    
count = count - 1
n = n + 2

for i in range(1,p):
    n = n + 2
    count = count - 1
    for j in range (count):
        print(f"  ", end = "")
    
    for k in range (n):
        print(f"* ", end = "")

    print()