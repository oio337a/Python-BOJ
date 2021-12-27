import sys

n, d, k, c = map(int, input().split())
li = [int(input()) for _ in range(n)]
left, right = 0, 0
ans = 0

while left != n:
    right = left + k
    case = set()
    flag = True
    for i in range(left, right):
        i %= n
        case.add(li[i])
        if li[i] == c:
            flag = False

    cnt = len(case)
    if flag:
        cnt += 1
    ans = max(ans, cnt)
    left += 1
print(ans)
