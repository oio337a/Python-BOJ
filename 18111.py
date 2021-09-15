# 높이의 최소값과 최대값을 찾고 그 범위만큼 반복문 돌려주며 비교.

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
pan = [list(map(int, input().split())) for i in range(n)]

mini = min(map(min, pan))
maxi = max(map(max, pan))
t = 1e9

for i in range(mini, maxi+1):
    p_cnt = 0
    m_cnt = 0
    for j in range(n):
        for k in range(m):
            h = pan[j][k] - i
            if h > 0:
                m_cnt += h
            elif h < 0:
                p_cnt -= h
    if m_cnt+b >= p_cnt:
        time = m_cnt*2 + p_cnt
        if t >= time:
            t = time
            result = i

print(t, result)
