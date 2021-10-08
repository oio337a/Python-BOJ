from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
food = [combinations(li, i) for i in range(1, n+1)]
answer = 1_000_000_000
for i in food:
    for j in i:

        sour = 1  # 곱셈
        bitter = 0  # 덧셈
        for s, b in j:

            sour *= s
            bitter += b
        answer = min(answer, abs(sour - bitter))  # 최솟값 갱신


print(answer)
