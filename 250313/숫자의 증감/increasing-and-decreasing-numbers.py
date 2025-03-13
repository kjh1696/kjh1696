string = input()
string = string.split()

C = str(string[0])
N = int(string[1])

i = 0
if C == 'A':
    for i in range(1,N+1):
        print(f"{i}", end = ' ')
elif C == 'D':
    for i in range(0,N):
        print(f"{N-i}", end = ' ')

        