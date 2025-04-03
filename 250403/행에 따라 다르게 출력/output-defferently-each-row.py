n = int(input())

cnt = 0

for i in range(n):

    for j in range (n):
        if i % 2 == 0:
            cnt = cnt + 1
            print(f"{cnt}", end = " ")
            
        else:
            cnt = cnt + 2
            print(f"{cnt}", end = " ")

    print()