
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

dic = {}
for i in range(n):
    dic[i+1] = set()
for j in range(m):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

# 정렬이 안되서..
# DFS


def dfs(start, dic):
    for i in dic[start]:
        if i not in visited_0:
            visited_0.append(i)
            dfs(i, dic)

# BFS


def bfs(s, dic):
    que = [s]
    while que:
        for i in dic[que.pop()]:
            if i not in visited_1:
                visited_1.append(i)
                que.append(i)


visited_0 = [v]
visited_1 = [v]
dfs(v, dic)
bfs(v, dic)
print(*visited_0)
print(*visited_1)
