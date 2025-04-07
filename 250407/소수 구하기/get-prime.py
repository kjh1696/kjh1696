

end = int(input())


# Please write your code here.
for i in range(1, end+1):

    my_count = 0
    for j in range(1,i+1):
        if i % j == 0:
            my_count = my_count + 1

    if my_count == 2 and i != 1:
        print(f"{i}", end = " ")

    
