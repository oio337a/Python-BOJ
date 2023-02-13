import sys
input = sys.stdin.readline

N = int(input())
level = list(map(int, input().split()))
fail = [0]*N
for i in range(1, N):
    if level[i-1] <= level[i]:
        fail[i] = fail[i-1] + 1
    else:
        fail[i] = fail[i-1]
q = int(input())
for _ in range(q):
    s, e = map(int, input().split())
    print(e - s - (fail[e - 1] - fail[s - 1]))


# 시간 초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# level = list(map(int, input().split()))
# fail = [0]*n

# for i in range(len(level)-1):
#     if level[i] > level[i+1]:
#         fail[i] = 1

# q = int(input())
# for _ in range(q):
#     s, e = map(int, input().split())
#     print(sum(fail[s-1:e-1]))
