number = input()
number = int(number)

cnt1 = 0
cnt2 = 0
cnt3 = 0

for i in range(number+1):
    if i == 0:
        continue
    elif i%12 == 0:
        cnt3 = cnt3 + 1
    elif i %6 == 0:
        cnt2 = cnt2 + 1
    elif i % 3 == 0:
        cnt2 = cnt2 + 1
    elif i %2 == 0:
        cnt1 = cnt1 + 1
  
        

print(f"{cnt1} {cnt2} {cnt3}")