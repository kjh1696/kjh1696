n = int(input())

for i in range(n): 
    for j in range(n):
        if i == 0:
            print(f"* ", end="")
        elif i <= j  and j % 2 != 0:
            print(f"* ", end="")
        else:
            print(f"  ", end = "")
    print()
