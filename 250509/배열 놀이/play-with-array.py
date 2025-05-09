n, q = map(int, input().split()) # n: 원소갯수, q: 질의개수
nn = list(map(int, input().split())) # n개의 원소 리스트

for i in range(q): # q개의 질의를 반복
    qq = list(map(int, input().split()))
    que = qq[0] # que: 질의 번호
    if que == 1: # 1번 답변: a번째 원소
        print(nn[qq[1] - 1]) 
    elif que == 2: # 2번 답변: 값이 b인 원소의 index / else 0
        for j in range(n):
            if nn[j] == qq[1]:
                print(j + 1)
                break
        else:
            print(0)
    else: # 3번 답변: nn의 s번째부터 e번째까지
        for j in range(qq[1] - 1, qq[2]):
            print(nn[j], end = " ")
            print()
