cnt = 0
for i in range(10):
    numbers = int(input())
    
    if numbers % 2 != 0:
        cnt = cnt + 1
    
print(f"{cnt}")
