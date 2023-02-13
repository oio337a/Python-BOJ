import sys
import collections
input = sys.stdin.readline

kdi = [-1, 1, -2, -2, -1, 1, 2, 2]
kdj = [-2, -2, -1, 1, 2, 2, -1, 1]


def move_k(i, j):  # 나이트 움직이기
    global t
    for a in range(8):
        ni, nj = i + kdi[a], j + kdj[a]
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
            visited[ni][nj] = 1
            t -= 1


qdi = [-1, -1, -1, 0, 1, 1, 1, 0]
qdj = [-1, 0, 1, 1, 1, 0, -1, -1]


def move_q(i, j):  # 퀸 움직이기
    global t
    for a in range(8):
        ni = i
        nj = j
        while True:
            ni, nj = ni+qdi[a], nj+qdj[a]
            if 0 <= ni < n and 0 <= nj < m:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    t -= 1
                elif visited[ni][nj] == 2:  # 말이 서있을 때
                    break
            else:
                break


'''초기 세팅'''
n, m = map(int, input().split())
visited = [[0]*m for _ in range(n)]
t = n * m
q = collections.deque()
k = collections.deque()

"""보드 입력"""
for i in range(3):
    s = collections.deque(input().split())
    for j in range(int(s.popleft())):
        a = int(s.popleft()) - 1  # 인덱스 맞추기
        b = int(s.popleft()) - 1
        visited[a][b] = 2  # 말 두기
        t -= 1
        if i == 0:
            q.append([a, b])
        elif i == 1:
            k.append([a, b])

while k:
    i, j = k.popleft()
    move_k(i, j)
while q:
    i, j = q.popleft()
    move_q(i, j)

print(t)
