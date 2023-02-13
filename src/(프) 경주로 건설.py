def solution(board):

    n = len(board)
    opend = [(0, 0, -1, 0)]  # y, x, direction, cost
    closed = [[-1 for _ in range(n)] for _ in range(n)]
    answer = -1

    while opend:
        y, x, d, c = opend.pop(0)
        if (y, x) == (n-1, n-1) and (answer == -1 or answer > c):
            answer = c

        neighbors = [(y, x-1), (y, x + 1), (y - 1, x), (y + 1, x)]
        for direction, (ny, nx) in enumerate(neighbors):
            if ny <= -1 or ny >= n or nx <= -1 or nx >= n:
                continue

            if board[ny][nx]:
                continue

            cost = c + (100 if d == direction or d == -1 else 600)
            if closed[ny][nx] != -1 and closed[ny][nx] < cost:
                continue

            opend.append((ny, nx, direction, cost))
            closed[ny][nx] = cost
    return answer
