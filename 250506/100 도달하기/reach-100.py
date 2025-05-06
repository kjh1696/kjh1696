num = int(input())
arr = [1, num]

for i in range (100):
    
    print(f"{arr[i]}", end = " ")
    arr.append(arr[i] + arr[i+1])

    if arr[i] >= 100:
        break
    
