"""
8 2
1 ~ 8 수열 에서 2개를 삭제하여 가장 긴 짝수의 수열 만들기
1 2 3 4 5 6 7 8
1 1 2 2 3 3 4 4

"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))

check = [0] * n

check[0] = 0 if li[0] % 2 == 0 else 1

for i in range(1, len(li)):
    if li[i] % 2 == 0:
        check[i] = check[i-1]
    else:
        check[i] = check[i-1] + 1

ans = 0
for i in range(n):
    l, r = 0, i
    while l <= r:
        mid = int((l+r)/2)
        if mid == 0:
            cnt = check[i]
        else:
            cnt = check[i] - check[mid-1]
        if cnt <= k:
            r = mid - 1
        else:
            l = mid + 1
    left = r + 1
    if left == 0:
        ans = max(ans, i - left + 1 - check[i])
    else:
        ans = max(ans, i - left + 1 - (check[i] - check[r]))


print(ans)
