number = int(input())


my_arr = list(map(int, input().split(" ")))

for val in reversed(my_arr):
    if val % 2 == 0:
        print(f"{val}", end = " ")
