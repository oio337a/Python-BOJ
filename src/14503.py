# 로봇 청소기
# https://www.acmicpc.net/problem/14503

"""
탐색 방향 순서 (왼, 아래, 오른쪽, 위쪽)
d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
current_x, current_y, d = map(int, input().split())
# d : 북 - 0, 동 - 1, 남 - 2, 서 - 3
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

moves = [
    [-1, 0], # 북쪽 방향으로 한 칸 이동
    [0, 1], # 동쪽 방향으로 한 칸 이동
    [1, 0], # 남쪽 방향으로 한 칸 이동
    [0, -1] # 서쪽 방향으로 한 칸 이동
]

# current_x + moves[d][0], current_y + moves[d][1] -> 현재 바라보고 있는 방향으로 한 칸 이동

# 시작점 청소한 것으로 업데이트
ans = 1
graph[current_x][current_y] = 2

def clean_here(current_x, current_y):
    global ans
    # 벽과 구분하기 위해서 청소된 구역은 2로 업데이트
    graph[current_x][current_y] = 2

    ans += 1

def turn_left(current_direction):
    if current_direction == 0:
        return 3

    else:
        return current_direction - 1


def is_cleanable(current_x, current_y, current_d):
    """
    현재 바라보고 있는 위치가 청소 가능한지 확인하는 함수
    """
    temp_x = current_x + moves[current_d][0]
    temp_y = current_y + moves[current_d][1]

    if 0 <= temp_x < n and 0 <= temp_y < m:
        if graph[temp_x][temp_y] == 0:
            return True

    return False

in_loop = True

while in_loop:
    for i in range(4):
        # 청소 할 수 있든 없든 회전은 하기 때문에 회전 먼저 해줌
        d = turn_left(d)

        # 만약 현재 바라보고 있는 위치가 청소 가능하다면
        if is_cleanable(current_x, current_y, d):
            # 한 칸 전진
            current_x += moves[d][0]
            current_y += moves[d][1]

            # 현 위치 청소
            clean_here(current_x, current_y)

            # 청소 후에는 다시 처음으로 돌아가므로 break
            break

        # 바라보고 있는 위치가 청소 불가능하다면 반복문 계속 진행
        else:
            continue

    # for문이 break 없이 종료되었다면 (네 방향 모두 청소 불가능하다면)
    else:
        # 뒤로 이동 -> 2바퀴 회전 후 이동하는 것과 같음 (실제 방향은 업데이트 X)
        temp_d = turn_left(d)
        temp_d = turn_left(temp_d)

        temp_x = current_x + moves[temp_d][0]
        temp_y = current_y + moves[temp_d][1]

        # 현재 위치의 뒷 방향이 범위 내에 있으면서 벽이 아닐 때
        if 0 <= temp_x < n and 0 <= temp_y < m and graph[temp_x][temp_y] != 1:
            # 뒤로 한 칸 이동
            current_x = temp_x
            current_y = temp_y

        # 뒤로 이동할 수 없을 때
        else:
            in_loop = False

print(ans)