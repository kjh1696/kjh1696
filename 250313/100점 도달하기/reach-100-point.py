N = int(input())
for i in range(N,100+1):
    if i >= 90:
        print(f"A", end = ' ')
    elif i >= 80:
        print(f"B", end = ' ')
    elif i >= 70:
        print(f"C", end = ' ')
    elif i >= 60:
        print(f"D", end = ' ')
    else:
        print(f"F", end = ' ')