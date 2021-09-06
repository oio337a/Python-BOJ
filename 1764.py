n, m = map(int, input().split())

a = set()
for _ in range(n):
    a.add(input())

b = set()
for _ in range(m):
    b.add(input())

answer = sorted(list(a & b))

print(len(answer))
for i in answer:
    print(i)

"""
시간 초과 why>??

import sys

a, b = map(int, sys.stdin.readline().split())

not_heard = []
not_saw = []

for _ in range(a):
    not_heard.append(sys.stdin.readline().rstrip())
for __ in range(b):
    not_saw.append(sys.stdin.readline().rstrip())

answer = []
for i in not_saw:
    if i in not_heard:
        answer.append(i)

print(len(answer))
answer.sort()
for j in answer:
    print(j)
"""
