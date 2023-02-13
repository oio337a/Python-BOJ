import sys
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

trains = [deque([0] * 20) for i in range(n+1)]
for i in range(m):
    command = list(input().split())
    if len(command) == 3:
        com, train, num = int(command[0]), int(command[1]), int(command[2])-1
        trains[train][num] = 1 if com == 1 else 0
    else:
        com, train = int(command[0]), int(command[1])
        if com == 3:
            trains[train][-1] = 0
            copy_train = deque(trains[train])
            copy_train.rotate(1)
            # copy_train
            trains[train] = copy.deepcopy(copy_train)
        else:
            trains[train][0] = 0
            copy_train = deque(trains[train])
            copy_train.rotate(-1)
            trains[train] = copy.deepcopy(copy_train)

trains.remove(trains[0])
answer = []
for i in trains:
    if i not in answer:
        answer.append(i)
print(len(answer))


"""
import  sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
train = [deque([0]*20) for _ in range(n)]
for _ in range(m):
    box=list(map(int,input().split()))
    if box[0]==1:
        train[box[1]-1][box[2]-1]=1
    elif box[0]==2:
        train[box[1]-1][box[2]-1]=0
    elif box[0]==3:
        train[box[1]-1].rotate(1)
        train[box[1]-1][0]=0
    else:
        train[box[1]-1].rotate(-1)
        train[box[1]-1][19]=0
answer=[]
for i in train:
    if i not in answer:
        answer.append(i)
print(len(answer))
"""


d = deque([1, 2, 3, 4])
d.rotate(1)

print(d)
