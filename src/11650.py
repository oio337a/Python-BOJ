import sys

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

li.sort()
for i in li:
    print(i[0], i[1])
