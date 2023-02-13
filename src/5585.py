# 거스름돈
# https://www.acmicpc.net/problem/5585

n = 1000 - int(input())
li = [500, 100, 50, 10, 5, 1]

ans = 0

for i in li:
    if n <= 0:
        break
    if n >= i:
        ans += n//i
        n = n%i

print(ans)
