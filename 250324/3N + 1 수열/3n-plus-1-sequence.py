n = int(input())

count = 0

while True:

    if n == 1:
        print(f"{count}")
        break

    
    if n % 2 == 0:
        n = n // 2
        count = count + 1
    else:
        n = 3 * n + 1
        count = count + 1


    
