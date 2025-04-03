n = int(input())

cnt1 = 0
temp = 0




for i in range(n):

    if i % 2 == 0:
        for j in range (n):
            cnt1 = cnt1 + 1
            print(f"{cnt1}", end = " ")

    elif i % 2 != 0:
        cnt1 += n+1
        for j in range (n,0,-1):
            cnt1 = cnt1 - 1
            print(f"{cnt1}", end = " ")
        cnt1 += n-1


        
    print()