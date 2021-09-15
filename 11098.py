# 첼시를 도와줘

import sys
input = sys.stdin.readline

n = int(input())
answer = []
for _ in range(n):
    a = int(input())
    li = []
    for i in range(a):
        a, b = input().split()
        li.append([int(a), b])
    li.sort(reverse=True)
    print(li[0][1])
