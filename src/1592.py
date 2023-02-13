
n, m, l = map(int, input().split())

player = [0]*n
cnt = 0
start = 0
while True:
    player[start] += 1
    if player[start] == m:
        print(cnt)
        break
    # 홀수
    elif player[start] % 2 == 1:
        start = (start+l) % n
    # 짝수
    else:
        start = (start+(n-l)) % n
    cnt += 1
