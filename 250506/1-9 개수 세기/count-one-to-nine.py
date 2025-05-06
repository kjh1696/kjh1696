num = int(input())
arr = list(map(int, input().split()))

for j in range(1,10):
    cnt = 0
    for i in range (len(arr)):
        if arr[i] == j:
            cnt += 1
    
    print(f"{cnt}", end = "\n")
