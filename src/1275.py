from math import e
import sys

input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = li[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]


def summit(start, end, node, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return summit(start, mid, node * 2, left, right) + summit(
        mid + 1, end, node * 2 + 1, left, right
    )


def update(start, end, node, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if not start == end:
        mid = (start + end) // 2
        update(start, mid, node * 2, index, diff)
        update(mid + 1, end, node * 2 + 1, index, diff)


n, q = map(int, input().split())
li = list(map(int, input().split()))
tree = [0] * (n * 4)

init(0, n - 1, 1)

for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(summit(0, n - 1, 1, x - 1, y - 1))
    diff = b - li[a - 1]
    li[a - 1] = b
    update(0, n - 1, 1, a - 1, diff)
