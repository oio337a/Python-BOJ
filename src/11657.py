# 타임머신
# https://www.acmicpc.net/problem/11657

# 최단 거리를 찾는 알고리즘
# 시간복잡도 O(VE) V: 정점 수, E: 간선 수
# 방향 그래프에서 음의 가중치를 지닌 간선이 존재할 때 사용
# 음의 순환이 있는 경우에는 최단 거리를 찾지 못함
#
# 작동 원리
# 시작 노드에 대해서 거리를 0으로 초기화, 나머지 노드는 거리를 무한으로 설정
# 정점 수(n) -1 만큼 다음 과정을 반복
# 매 반복 마다 모든 간선 확인
# 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, 거리 정보 갱신
# n-1번 반복 이후, n번째 반복에서도 거리 값이 갱신된다면 음수 순환이 존재
# 다익스트라와의 차이점은 매 반복마다 모든 간선을 확인한다는 것입니다.
# 다익스트라는 방문하지 않는 노드 중에서 최단 거리가 가장 가까운 노드만을 방문했습니다.

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = []
dist = [INF] * (n+1)

# 그래프 생성
for _ in range(m):
    u, v, w = map(int, input().split()) # 노드, 인접 노드, 가중치
    edges.append((u, v, w))

# 벨만 포드 알고리즘
def bf(start):
    dist[start] = 0  # 시작 노드에 대해서 거리를 0으로 초기화
    for i in range(n): # 정점의 수만큼 반복
        for j in range(m): # 모든 간선 확인
            node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 들려 다른 노드로 이동하는 거리가 더 짧은 경우 값 갱신
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                if i == n-1:
                    return True
    return False

negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    for i in range(2, n+1): # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
        if dist[i] == INF: # 도달할 수 없는 경우 -1 출력
            print('-1')
        else: # 도달하면 거리 출력
            print(dist[i])

