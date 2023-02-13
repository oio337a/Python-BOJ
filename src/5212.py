import sys
import copy
input = sys.stdin.readline

R, C = map(int, input().split())

matrix = [list(input()) for _ in range(R)]
result = copy.deepcopy(matrix)

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

for y in range(R):  # 주변 3면이상이 '.' 인지 확인 후 바꿔 주기
    for x in range(C):
        count = 0
        if matrix[y][x] == '.':
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < R and 0 <= nx < C:  # 보드 안에 있는데 '.' 일 경우
                if matrix[ny][nx] == '.':
                    count += 1
            else:               # 보드 밖일 경우
                count += 1
        if count >= 3:
            result[y][x] = '.'

start_y, end_y = 0, 0
for i in range(R):
    if 'X' in result[i]:  # 첫 'X' 찾기
        start_y = i
        break
for i in range(R-1, -1, -1):
    if 'X' in result[i]:  # 마지막 'X' 찾기
        end_y = i
        break

temp = []
for j in range(C):
    for i in range(start_y, end_y + 1):
        if 'X' == result[i][j]:
            temp.append(j)
            break

for y in range(start_y, end_y + 1):
    print("". join(result[y][temp[0]:temp[-1]+1]))
