import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

trains = [[0] * 21 for i in range(n)]
for i in range(m):
    command = list(input().split())
    if len(command) == 3:
        com, train, num = int(command[0]), int(command[1]), int(command[2])
        trains[train][num] = 1 if com == 1 else 0
    else:
        com, train = int(command[0]), int(command[1])
        if com == 3:
            trains[train][-1] == 0
            copy_train = deque(trains[train])
            copy_train.rotate(1)
            trains[train] = copy_train
        else:
            trains[train][0] == 0
            copy_train = deque(trains[train])
            copy_train.rotate(-1)
            trains[train] = copy_train

answer = []
for i in trains:
    if i not in answer:
        answer.append(i)
print(len(answer))
