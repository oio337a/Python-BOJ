'''
1 2 3 4 5 6 7 8 9 10

3 4 5 6 7 8 9 10 11 12
x     x     x        x
    x         x
        x
  x       x      x
        x
    
    (누적합)

구간 학생 수 - (누적합[구간 마지막값] - 누적합[구간 시작값])
'''


import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
sleep = [0] * (N+3)
check_code = [0] * (N+3)

for i in map(int, input().split()):
    sleep[i] = 1
for i in map(int, input().split()):
    if sleep[i]:
        continue
    for j in range(i, N+3, i):
        if not sleep[j]:
            check_code[j] = 1

prefix = [check_code[0]]
for i in range(1, N+3):
    prefix.append(prefix[-1] + check_code[i])
    # 각 학생번호 i 까지 출석한 학생들의 합

for _ in range(M):
    s, e = map(int, input().split())
    print(e-s+1 - (prefix[e] - prefix[s-1]))


# student = [0]*(N+3)

# for i in check_code:
#     for j in range(N):
#         if i * j <= N+3:
#             student[i*j] = 1

# for i in sleep:
#     for j in range(N):
#         if i * j <= N+3:
#             student[i*j] = 0

# for _ in range(M):
#     a, b = map(int, input().split())
#     print(student[a:b+1].count(0))
