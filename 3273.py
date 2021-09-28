import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
x = int(input())
li.sort()
l, r = 0, n-1
cnt = 0

while l < r:
    num = li[l] + li[r]
    if num == x:
        cnt += 1
    if num < x:
        l += 1
    else:
        r -= 1
print(cnt)
