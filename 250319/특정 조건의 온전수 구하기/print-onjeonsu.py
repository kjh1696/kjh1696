N = int(input())

for i in range(1, N+1):
    if i % 2 == 0:  # 2로 나누어 떨어지는 경우 제외
        continue
    if str(i)[-1] == '5':  # 일의 자리가 5인 경우 제외
        continue
    if i % 3 == 0 and i % 9 != 0:  # 3으로 나누어 떨어지면서 9로 나누어 떨어지지 않는 경우 제외
        continue
    print(i, end=' ')
