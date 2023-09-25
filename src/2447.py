
def counting_star(n):
    global board

    if n == 3:
        board[0][:3] = board[2][:3] = ['*']*3
        board[1][:3] = ['*', ' ', '*']
        return
        # ***
        # * *
        # ***

    a = n // 3  # 3으로 나눈 구역
    counting_star(a)  # 3
    for i in range(3):  # 0 1 2
        for j in range(3):  # 0 1 2
            if (i == 1 and j == 1) or (i == 0 and j == 0):
                continue   # 가운데 영역 건너 뛰기
            for k in range(a):
                board[a*i+k][a*j:a*(j+1)] = board[k][:a]


N = int(input())
board = [[' ' for i in range(N)] for i in range(N)]
counting_star(N)

for i in board:
    print(*i, sep='')
