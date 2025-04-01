n = int(input())

first = 1
second = n

for i in range(1,2*n+1):

    if i % 2 == 0:
        for j in range(first):
            print(f"* ", end = "")
        first = first + 1
        print()
    
    elif i%2 != 0:
        for k in range(second):
            print(f"* ", end = "")
        second = second - 1
        print()