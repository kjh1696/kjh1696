n = int(input())
p = n

count = 1
a = True

if n > 0:
    
    while n != 0:
        n = n - 1

        for i in range(n):
            print(f"  ", end = "")

        for j in range(count):
            print(f"@ ", end = "")

        count = count + 1

        print()
        
count = count - 1

if n <= 0:

    while n != p:

        count = count - 1

        for i in range(count):
            print(f"@ ", end = "")

        for j in range(n):
            print(f"   ", end = "")
                
        n = n + 1
                
        print()


