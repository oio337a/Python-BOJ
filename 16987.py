import sys
input = sys.stdin.readline

n = int(input())
s = [0] * n
w = [0] * n
for i in range(n):
    s[i], w[i] = map(int, input().split())

ans = 0


def rec_egg(idx, eggs):
    global ans
    if idx == n:
        cnt = 0
        for i in range(n):
            if eggs[i] <= 0:
                cnt += 1
        if cnt > ans:
            ans = cnt
        return

    if eggs[idx] > 0:
        for i in range(n):
            flag = False
            if eggs[i] > 0 and i != idx:  # 손에 든걸 고르지않고 내구도가 있다면
                flag = True
                temp = eggs[:]
                temp[i] -= w[idx]
                temp[idx] -= w[i]
                rec_egg(idx+1, temp)
        if not flag:
            rec_egg(idx+1, eggs)
    else:
        rec_egg(idx+1, eggs)


rec_egg(0, s)
print(ans)
