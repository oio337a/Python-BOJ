parent = [0] * (n + 1)
level = [0] + [1] * n

# 초기에 각 노드는 자기 자신을 루트 노드로 가지고 있다.
for i in range(1, n+1):
    parent[i] = i

# Find를 통해 반환 되는 값은 그 집합의 대푯값(해당 트리(집합)의 루트노드)이다.
def find(u):
    if (u == parent[u]):
        return u
    return parent[u] == find(parent[u])

# 해당 노드는 루트 노드를 찾기 위해 부모값을 통해서 Find함수를 호출한다.
# 이동하며 모든 노드의 루트노드도 갱신한다.

# Union은 Find를통해 두 개의 트리의 루트 노드를 이용해 하나의 트리로 합치게 된다.
def union(u, v):
    u = find(u)
    v = find(v)

    if (u == v):
        return
    if (level[u] > level[v]):
        parent[u] = v
        level[u] += level[v]
    else:
        parent[v] = u
        level[v] += level[u]

# u와 v 를 합치는 함수. 루트가 같다면 돌아가고 아니라면 한쪽 트리를 다른쪽에 이어준다(루트노드끼리)
# (level이용 높이가 낮은 트리를 높은 트리 아래로 들어가게끔 설계)