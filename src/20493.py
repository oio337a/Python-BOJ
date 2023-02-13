import sys
input = sys.stdin.readline

N, T = map(int, input().split())
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
i = X = Y = 0
li = [0]
for _ in range(N):
    time, s = input().split()
    time = int(time)
    t = time-li[-1]
    li.append(time)
    x, y = direction[i][0], direction[i][1]
    X += t*x
    Y += t*y
    i += 1 if s == 'right' else -1
    i = i % 4
t = T-li[-1]
x, y = direction[i][0], direction[i][1]
X += t*x
Y += t*y
print(X, Y)
