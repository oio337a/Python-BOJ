# 물병
# https://www.acmicpc.net/problem/1052

# 문제 접근법이 중요하다.
# 뭔가 2진법같이 생겼다.
# 2진법으로 풀어보자

# N을 이진법으로 바꾸면 (ex, 11 => 1011)
# 물병: 1,1,1,1,1,1,1,1,1,1,1
# 합치기: 2,2,2,2,2,1
# 합치기: 4,4,2,1
# 합치기: 8,2,1
# 결론: N을 이진법으로 바꾼 수의 1의 개수가
# 물을 최대로 합친 후의 물병의 개수이다.
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

purchased_water_bottle_cnt = 0

while bin(N).count('1') > K:
    idx = bin(N)[::-1].index('1')
    purchased_water_bottle_cnt += 2**idx
    N += 2**idx

print(purchased_water_bottle_cnt)
