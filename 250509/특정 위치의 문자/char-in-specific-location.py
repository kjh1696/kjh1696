word = ['L', 'E', 'B', 'R', 'O', 'S']

spell = input()

for i in range (len(word)):
    if word[i] == spell:
        print(f"{i}")
        break

if i == (len(word)-1) and word[i] != word[len(word)]:
    print(f"None")


