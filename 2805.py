import sys
input = sys.stdin.readline

"""
길이가 5와 2 인 나무를 집에 들고간다.
"""
n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    print(mid)
    cut_tree = 0
    for i in tree:
        if i >= mid:
            cut_tree += i - mid
    if cut_tree >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
