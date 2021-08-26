
N, M = map(int, input().split())

ball = [i for i in range(1, N+1)]

for i in range(M):
    temp = 0
    a, b = map(int, input().split())
    temp = ball[a-1]
    ball[a-1] = ball[b-1]
    ball[b-1] = temp

for _ in range(len(ball)):
    print(ball[_], end=' ')
