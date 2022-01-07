import sys
input = sys.stdin.readline


def init(start, end, node):  # 세그먼트 트리 만들기
    if start == end:
        tree[node] = nList[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]


def summit(start, end, node, left, right):  # 구간합 구하기
    # left 와 right가 범위에서 벗어났기 때문에 return
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return summit(start, mid, node * 2, left, right) + summit(mid + 1, end, node * 2 + 1, left, right)


def update(start, end, node, index, diff):  # 인덱스 값 바꾸기
    # index 범위 벗어 나면 return
    if index < start or index > end:
        return

    tree[node] += diff
    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, index, diff)
    update(mid + 1, end, node * 2 + 1, index, diff)


# 입력받기 & 초기값 설정
n, m, k = map(int, input().split())
nList = [int(input()) for _ in range(n)]
tree = [0] * ((4 * n))

# 트리 만드는 함수 실행
init(0, n - 1, 1)

# 커멘드 입력받기 & 출력
for i in range(m + k):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        cmd[1] -= 1
        diff = cmd[2] - nList[cmd[1]]
        nList[cmd[1]] = cmd[2]
        update(0, n - 1, 1, cmd[1], diff)
    elif cmd[0] == 2:
        print(summit(0, n - 1, 1, cmd[1] - 1, cmd[2] - 1))
