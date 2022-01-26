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


"""
key = 물의 양(liter), value = 물병 개수
합칠 수 있을 만큼 합치기 -> 가지고 있는 물병의 개수가 K개 이하인지 판별
-> K개 보다 크다면 합치기 위한 필요한 최소 물 구입

import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())

bottle = defaultdict(int)
bottle[1] = N

liter, buy = 1, 0
while 1:
    while liter in bottle: 
        #해당 liter을 가진 물병이 1병 이상 존재할 때, 합칠 수 있을 만큼 합침
        if bottle[liter] > 1:
            bottle[liter * 2] += bottle[liter] // 2
            bottle[liter] %= 2
        liter *= 2 
        
    if sum(list(bottle.values())) <= K: #총 가지고 있는 물병의 양이 K개 이하일 경우 반복문 종료
        break

    #합칠 수 있는 최소 물병의 수를 구입
    liters = [liter for liter in bottle if bottle[liter] > 0]
    buy += liters[1] - liters[0]
    bottle[liters[0]] = 0
    bottle[liters[1]] = 0
    bottle[liters[1] * 2] += 1
    liter = liters[1] * 2
        
print(buy)
"""