"""
*****  
*   *  
* * *  
*   *  
*****  
(4*n-3)
"""


def draw(n, idx):
    if n == 1:
        board[idx][idx] = '*'
        return
    l = 4 * n - 3

    for i in range(idx, l+idx):
        board[idx][i] = '*'
        board[idx+l-1][i] = '*'

        board[i][idx] = '*'
        board[i][idx+l-1] = '*'
    return draw(n-1, idx+2)


n = int(input())
lens = 4 * n - 3

board = [[' '] * lens for _ in range(lens)]

draw(n, 0)

for i in range(lens):
    for j in range(lens):
        print(board[i][j], end="")
    print()
