n = int(input())

cnt1 = n
cnt2 = 1

for j in range(n):
    for i in range(1,n+1,1):
        if i % 2 == 0:
            print(cnt1, end="")
        else:
            print(cnt2, end="")
    
    cnt1 = cnt1 - 1
    cnt2 = cnt2 + 1

    print()