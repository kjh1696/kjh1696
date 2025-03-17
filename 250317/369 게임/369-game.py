number = int(input())
start = 1

while start <= number:
    str_number = str(start)
    # 3의 배수이거나 숫자에 3,6,9 포함 시
    if (start % 3 == 0) or ('3' in str_number) or ('6' in str_number) or ('9' in str_number):
        print("0", end=" ")
    else:
        print(start, end=" ")
    start += 1
