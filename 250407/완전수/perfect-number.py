start, end = map(int, input().split())

# Please write your code here.

count = 0
for i in range(start, end+1):

    sum = 0
    for j in range(1,i):
        if i % j == 0:
            sum = sum + j

    if sum == i:
        count = count + 1

print(f"{count}")
