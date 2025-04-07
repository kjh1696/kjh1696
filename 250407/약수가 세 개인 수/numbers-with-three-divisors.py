arr = input().split(" ")

start = int(arr[0])
end = int(arr[1])

# Please write your code here.

count = 0
for i in range(start, end+1):

    my_count = 0
    for j in range(1,i+1):
        if i % j == 0:
            my_count = my_count + 1

    if my_count == 3:
        count = count + 1

print(f"{count}")
