cnt1 = 0
cnt2 = 0
for n in range(10):
    i = int(input())
    if i % 3 == 0:
        cnt1 = cnt1 + 1
    if i % 5 == 0:
        cnt2 = cnt2 + 1

print(f"{cnt1} {cnt2}")
