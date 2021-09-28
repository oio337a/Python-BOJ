from types import coroutine
from _collections import deque
import sys
from collections import deque
input = sys.stdin.readline

"""
트럭이 하중보다 작으면 지나간다. 시간 += 길이
트럭의 합이 하중보다 작으면 지나간다. 시간 -= 1

--- 3 3 0
--- 4 6 2 
--- 5 9 4 
---- 4 4 0
---- 5 8
---- 6 12

"""
# n은 트럭의 수
# w는 다리의 길이
# L은 다리의 최대하중
"""
틀림 
반례 
5 2 10
9 4 8 1 5
출력값 9 나와야 하지만 10 나옴
이유는 값들을 저장하고 한번에 처리하다 보니 
중간에 차량이 지나가고 다리를 건널 수 있는 차량이 생겨도
지나가지 않는다.
느낀점
1초씩 증가하는 문제는 1초씩 늘려가면서 리스트 추가 삭제 하는게 좋다.

n, w, l = map(int, input().split())
car = deque(map(int, input().split()))


t = 0
while car:
    cross = deque([car.popleft()])
    cross_cars_w = sum(cross)
    while cross_cars_w <= l:
        if len(cross) > w:  # 다리 길이보다 건너는 차가 많을 경우
            t += 1
            cross.popleft()
        cross_cars_w = sum(cross)
        if len(car) != 0 and cross_cars_w + car[0] <= l:
            cross.append(car.popleft())
        else:
            break
    if len(cross) == 1:
        t += w
    else:
        t += w + (len(cross) - 1)
    cross = []

print(t+1)
"""

N, W, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))

answer = 0
bridge = deque([0 for _ in range(W)])

while trucks:
    bridge.popleft()
    if len(bridge) < W:
        if sum(bridge) + trucks[0] <= L:
            truck = trucks.popleft()
            bridge.append(truck)
        else:
            bridge.append(0)
    answer += 1
answer += W
print(answer)
