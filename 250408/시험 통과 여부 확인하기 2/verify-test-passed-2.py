number = int(input())

count = 0
for i in range(number):
    my_arr = list(map(float, input().split()))

    if sum(my_arr) / 4 >= 60:
        print(f"pass")
        count = count + 1
    else:
        print(f"fail")

print(f"{count}", end = "")