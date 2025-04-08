

end = int(input())


# Please write your code here.
for i in range(end):

    inputs = input()
    inputs = inputs.split(" ")

    number_a = int(inputs[0])
    number_b = int(inputs[1])

    number = 0
    for i in range(number_a, number_b+1):
        if i % 2 == 0:
            number = number + i
    
    print(f"{number}", end = "")
    print()

    
