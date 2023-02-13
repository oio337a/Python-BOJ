"""
봄 
- 나이만큼 양분 먹고 나이 +1
- 같은 칸에 나무가 여럿이라면 나이가 어린 나무부터 양분 섭취
- 칸의 양분이 나무의 나이보다 적다면 나무는 죽는다

여름
- 죽은나무 양분으로 변함
- 죽은나무 나이 // 2

가을
- 번식 (5의 배수인 나무만 해당)
- 인접한 8개의 칸에 나이 1인 나무 +1
- 땅을 벗어나면 제외

겨울
- 양분 추가
"""
from collections import deque
import sys
input = sys.stdin.readline


def spring():
    for i in range(n):
        for j in range(n):
            len_t = len(t[i][j])
            for k in range(len_t):
                if t[i][j][k] <= no[i][j]:
                    no[i][j] -= t[i][j][k]
                    t[i][j][k] += 1
                else:
                    for _ in range(k, len_t):
                        no[i][j] += t[i][j].pop() // 2
                    break


def fall():
    for i in range(n):
        for j in range(n):
            for k in t[i][j]:
                if k % 5 == 0:
                    for l in range(8):
                        x = i + dx[l]
                        y = j + dy[l]
                        if 0 <= x < n and 0 <= y < n:
                            t[x][y].appendleft(1)
            no[i][j] += s[i][j]


dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
n, m, k = map(int, input().split())
s = []
t = [[deque() for i in range(n)] for i in range(n)]
no = [[5] * n for i in range(n)]
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(n):
    x, y, z = map(int, input().split())
    t[x - 1][y - 1].append(z)
for i in range(k):
    spring()
    fall()
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(t[i][j])
print(cnt)
