import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0 for _ in range(32001)]
graph = [[] for i in range(32001)]
queue = deque()

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    student = queue.popleft()
    print(student, end=' ')
    for j in graph[student]:
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append(j)