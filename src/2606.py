# # DFS
# import sys
# input = sys.stdin.readline

# dic = {}
# for i in range(int(input())):
#     dic[i+1] = set()
# for j in range(int(input())):
#     a, b = map(int, input().split())
#     dic[a].add(b)
#     dic[b].add(a)


# def dfs(s, dic):
#     for i in dic[s]:
#         if i not in visited:
#             visited.append(i)
#             dfs(i, dic)


# visited = []
# dfs(1, dic)
# print(len(visited)-1)

# BFS

import sys
input = sys.stdin.readline

dic = {}
for i in range(int(input())):
    dic[i+1] = set()
for j in range(int(input())):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)


def bfs(s, dic):
    que = [s]
    while que:
        for i in dic[que.pop()]:
            if i not in visited:
                visited.append(i)
                que.append(i)


visited = []
bfs(1, dic)
print(len(visited)-1)
