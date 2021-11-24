"""
다익스트라 알고리즘 - 최단 경로 탐색 알고리즘

1. 출발노드 설정.
2. 출발노드 기준으로 각 노드 최소 비용 저장
3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드 선택
4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소비용 갱신
위 3, 4 과정 반복

1. 지름길이 없을때 자기 자신을 default로 가지는 arr 배열을 생성한다.
2. 0부터 목적지까지 돈다.
3. 이전지점+1 이 더 작다면 update해준다.
4. 지름길이 있다면 저장된 길이 (distance[타겟점])와 뻗어나간 길이 (w + distance[시작점]) 중 작은 것으로 update해준다.
"""

# import sys
# input = sys.stdin.readline

# n, d = map(int, input().split())
# arr = [[] for _ in range(10001)]
# for _ in range(n):
#     start, end, l = map(int, input().split())
#     arr[start].append([l, end])
# distance = [i for i in range(d+1)]

# for i in range(d+1):
#     if i != 0:
#         distance[i] = min(distance[i], distance[i-1] + 1)
#         for w, e in arr[i]:
#             if e <= d and distance[e] > w + distance[i]:
#                 distance[e] = w + distance[i]
# print(distance[d])

import sys
input = sys.stdin.readline

N, D = map(int, input().split())
arr = [[] for _ in range(10001)]
for _ in range(N):
    s, e, w = map(int, input().split())
    arr[s].append([w, e])
distance = [i for i in range(D+1)]

for i in range(D+1):
    if i != 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    for w, e in arr[i]:
        if e <= D and distance[e] > w + distance[i]:
            distance[e] = w + distance[i]

print(distance[D])
