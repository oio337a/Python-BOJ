# 용액
# https://www.acmicpc.net/problem/2467

import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

s, e = 0, n-1
ans_L = ans_R = 0
mini = sys.maxsize

while s < e:
    hap = li[s] + li[e]

    if abs(hap) < mini:
        ans_L = s
        ans_R = e
        mini = abs(hap)

    # e -= 1 if hap > 0 else s += 1    증감 연산자 삼항연산 불가

    if hap == 0:
        break
    elif hap > 0:
        e -= 1
    else:
        s += 1

print(li[ans_L], li[ans_R])

