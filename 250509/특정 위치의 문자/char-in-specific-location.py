word = ['L', 'E', 'B', 'R', 'O', 'S']

spell = input()

for i in range (len(word)):
    if word[i] == spell:
        print(f"{i}")
        break

else:
    print(f"None")
