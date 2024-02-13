# 트리의 높이와 너비
import sys

# dfs : 현재 노드 번호가 num이고 깊이가 depth일 때 노드 위치를 구하는 함수
def dfs(num, depth):
    global cnt
    # Base Case : 노드 번호가 유효하지 않은 경우
    if num == -1:
        return
    # 현재 depth가 dictionary에 없다면 해당 깊이에서의 [최소 위치, 최대 위치]로 초기화
    if depth not in res:
        res[depth] = [9876543210, -9876543210]
    # 왼쪽 서브트리
    dfs(tr[num][0], depth + 1)
    # 최소, 최대 너비 갱신
    res[depth][0] = min(res[depth][0], cnt)
    res[depth][1] = max(res[depth][1], cnt)
    # 위치 증가
    cnt += 1
    # 오른쪽 서브트리
    dfs(tr[num][1], depth + 1)

# 입력부
n = int(sys.stdin.readline())

# tr : N X 2 행렬로, i번째 행 0번째 열은 왼쪽 자식, i번째 행 1번째 열은 오른쪽 자식을 저장
tr = [[-1] * 2 for _ in range(n + 1)]

# res : depth를 key, [최소 위치, 최대 위치]를 value로 하는 dictionary
res = dict()
cnt = 1

# ind : 전입 차수, 루트 판별용도
ind = [0] * (n + 1)

# 입력부
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    if b != -1:
        tr[a][0] = b
        ind[b] += 1
    if c != -1:
        tr[a][1] = c
        ind[c] += 1
        
root = -1
for i in range(1, n + 1):
    # 루트이기에 전입 차수는 0
    if not ind[i]:
        root = i

# 중위 순회
dfs(root, 1)
ans = []
for i in res:
    ans.append((res[i][1] - res[i][0] + 1, i))
    
# 문제 조건에 따라 정렬 후 정답 출력
ans.sort(key=lambda x : (-x[0], x[1]))
print(ans[0][1], ans[0][0])