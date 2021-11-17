"""
1. 주식 하나를 산다.
2. 원하는 만큼 가지고 있는 주식을 판다.
3. 아무것도 안한다.
"""


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    days = int(input())
    jusik = list(map(int, input().split()))
    suik = []

    mx = jusik[-1]
    for i in range(days-2, -1, -1):
        if jusik[i] > mx:
            mx = jusik[i]
        else:
            suik.append(mx-jusik[i])
    print(sum(suik))
