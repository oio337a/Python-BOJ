import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))
ans = 0

for i in range(1, w-1):
    left = max(block[:i])
    rigth = max(block[i+1:])
    m = min(left, rigth)

    # 좌우의 블럭 높이의 최댓값 중 작은 값이 현재 블록보다 크다면
    # 반대쪽 값도 그 블럭보다 크다. 따라서 작은 값 - 현재블럭 높이 만큼 ans에 저장.
    if m > block[i]:
        ans += m - block[i]
print(ans)
