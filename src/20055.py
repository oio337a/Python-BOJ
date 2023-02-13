from collections import deque
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
li = deque(list(map(int, input().split())))  # belt
box = deque([0]*n)
res = 0

while 1:
    li.rotate(1)  # [1,2,3,4,5]  [5,1,2,3,4] [4,5,1,2,3]
    box.rotate(1)
    box[-1] = 0  # 박스가 떨어진다.
    if sum(box):
        for i in range(n-2, -1, -1):
            if box[i] == 1 and box[i+1] == 0 and li[i+1] >= 1:
                box[i+1] = 1
                box[i] = 0
                li[i+1] -= 1
        box[-1] = 0
    if box[0] == 0 and li[0] >= 1:
        box[0] = 1
        li[0] -= 1
    res += 1
    if li.count(0) >= k:
        break

print(res)
