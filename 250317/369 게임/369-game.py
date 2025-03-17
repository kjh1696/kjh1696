number = int(input())
start = 1

while start <= number:
    if start % 3 ==0:
        print(f"0", end = " ")
        start = start + 1
    else:
        str_number = str(start)
        for i in range(len(str_number)):
            count = 0
            if str_number[i] == '3' or str_number[i] == '6' or str_number[i] == '9':
                count = count + 1
        if count > 0:
            print(f"0", end = " ")
            start = start + 1  
        else:
            print(f"{start}", end = " ")
            start = start + 1
               