n = int(input())

for i in range(n,0,-1):
    print(f"*"*i ,end = "")
    print(f" " * (n-i),end =  "")
    print(f" " * (n-i),end =  "")
    print(f"*"*i,end = "")

    print()