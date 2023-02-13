import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(money, cnt):
    if check[money] >= cnt:
        return
    if money == X:
        check[money] = cnt
        for i in range(4):
            ans[i] = used[i]
        return
    check[money] = cnt
    if coin[0] >= used[0] + 5 and money + 5 <= X:
        used[0] += 5
        dfs(money + 5, cnt + 5)
        used[0] -= 5
    if coin[1] > used[1] and money + 5 <= X:
        used[1] += 1
        dfs(money + 5, cnt + 1)
        used[1] -= 1
    if coin[2] > used[2] and money + 10 <= X:
        used[2] += 1
        dfs(money + 10, cnt + 1)
        used[2] -= 1
    if coin[3] > used[3] and money + 25 <= X:
        used[3] += 1
        dfs(money + 25, cnt + 1)
        used[3] -= 1


coin = [0] * 4
ans = [0] * 4
check = [0] * 10001
used = [0] * 4

X, coin[0], coin[1], coin[2], coin[3] = map(int, input().split())
x = X % 5
if coin[0] < x:
    print(0, 0, 0, 0)
    exit(0)
for i in range(X + 1):
    check[i] = -1
used[0], money = x, x
dfs(money, money)

print(*ans)
