arr_first = list(map(int, input().split()))
arr_second = list(map(int, input().split()))

count = 0
for i in range (arr_first[0]):
    if arr_second[i] == arr_first[1]:
        count = count + 1

print(f"{count}")