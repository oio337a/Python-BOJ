import sys
input = sys.stdin.readline

r, c = map(int, input().split())

words = [list(input().rstrip()) for _ in range(r)]
li = []

for i in range(r):
    temp = ""
    length = 0
    for j in range(c):
        if words[i][j] == '#':
            if length >= 2:
                li.append(temp)
            length = 0
            temp = ""
        else:
            temp += words[i][j]
            length += 1
    if len(temp) >= 2:
        li.append(temp)

for i in range(c):
    temp = ""
    length = 0
    for j in range(r):
        if words[j][i] == '#':
            if length >= 2:
                li.append(temp)
            length = 0
            temp = ""
        else:
            temp += words[j][i]
            length += 1
    if len(temp) >= 2:
        li.append(temp)

li.sort()
print(li[0])
