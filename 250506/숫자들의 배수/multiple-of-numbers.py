num = int(input())

count = 0;
for i in range(1, 100000):
    print(f"{num * i}", end = " ")
    
    if (num * i) % 5 == 0:
        count = count + 1
    
    if count == 2:
        break
