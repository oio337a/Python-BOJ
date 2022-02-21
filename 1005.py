import sys
from collections import deque

T=int(sys.stdin.readline())

for _ in range(T):
    N,K=map(int,sys.stdin.readline().split())#건물수 건물간의 건설순서규칙
    building=[0]+list(map(int,sys.stdin.readline().split()))#각 건물들의 건설시간
    tree=[[] for _ in range(N+1)]#건설순서규칙
    inDegree=[0 for _ in range(N+1)]#진입차수
    DP=[0 for _ in range(N+1)]#해당 건물까지 걸리는 시간

    for _ in range(K):#건설규칙 저장
        a,b=map(int,sys.stdin.readline().split())
        tree[a].append(b)
        inDegree[b]+=1

    q = deque()
    for i in range(1,N+1):#진입차수 0인거 찾아서 큐에 넣기
        if inDegree[i]==0:
            q.append(i)
            DP[i]=building[i]

    while q:
        a=q.popleft()
        for i in tree[a]:
            inDegree[i]-=1#진입차수 줄이고 비용갱신
            DP[i]=max(DP[a]+building[i],DP[i])#DP를 이용해 건설비용 갱신
            if inDegree[i]==0:
                q.append(i)


    answer=int(sys.stdin.readline())
    print(DP[answer])
#
# DP 풀이
# import sys
# sys.setrecursionlimit(10**5)
# def TOP_DOWN(node):
#     if not grp[node]: # 더이상 부모노드가 없을 때
#         dpTABLE[node] = val[node]
#         return dpTABLE[node]
#     if dpTABLE[node] >= 0: # 기록된 값이 있을 때
#         return dpTABLE[node]
#     MAX = 0
#     for new_node in grp[node]:
#         MAX = max(MAX, TOP_DOWN(new_node))
#     dpTABLE[node] = val[node] + MAX
#     return dpTABLE[node]
#
# In = lambda : sys.stdin.readline().rstrip()
# MIS = lambda : map(int, In().split())
# T = int(In())
# for t in range(T):
#     N, R = MIS()
#     val = [0]+[*MIS()]
#     grp = [[] for i in range(N+1)]
#     check = [0]*(N+1)
#     for r in range(R):
#         a,b = MIS()
#         grp[b].append(a)
#     TARGET_NODE = int(In())
#     dpTABLE = [-1]*(N+1)
#     check = [0]*(N+1)
#     TOP_DOWN(TARGET_NODE)
#     if grp[TARGET_NODE]:
#         print(val[TARGET_NODE] + max(dpTABLE[i] for i in grp[TARGET_NODE]))
#     else:
#         print(val[TARGET_NODE])