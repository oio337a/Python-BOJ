import sys

input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    li.append(input())

count = 0
num = 0
for i in range(n):
    for j in range(n-1):
        if li[i][j] == '.' and li[i][j+1] == '.':
            count += 1
            break
for i in range(n):
    for j in range(n-1):
        if li[j][i] == '.' and li[j+1][i] == '.':
            num += 1
            break
print(count, num)
