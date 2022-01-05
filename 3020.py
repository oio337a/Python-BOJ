import sys
input = sys.stdin.readline

n, h = map(int, input().split())

suksoon = [0] * (h + 1)
jongyousuk = [0] * (h + 1)

min_break = n
min_cnt = 0

for i in range(n):
    if i % 2 == 0:
        suksoon[int(input())] += 1
    else:
        jongyousuk[int(input())] += 1

for i in range(h - 1, 0, -1):
    suksoon[i] += suksoon[i + 1]
    jongyousuk[i] += jongyousuk[i + 1]

for i in range(1, h + 1):
    if min_break > (suksoon[i] + jongyousuk[h - i + 1]):
        min_break = (suksoon[i] + jongyousuk[h - i + 1])
        min_cnt = 1
    elif min_break == (suksoon[i] + jongyousuk[h - i + 1]):
        min_cnt += 1

# print(min_break, min_cnt)
