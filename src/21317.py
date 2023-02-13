import sys
input = sys.stdin.readline

"""
작은 점프, 큰 점프 사용하여 도착지까지 갔을 경우 에너지 값 저장
최소 값 출력,
매우 큰 점프 사용 유무 확인 후 사용.
"""
n = int(input())
stones = [0] + list(tuple(map(int, input().split())) for _ in range(n-1))
k = int(input())

arr = []


def dfs(idx, use_big_jump, energy):
    if idx == n:  # 최종 돌까지 갔을 때 든 에너지 총합을 arr에 저장 후 리턴
        arr.append(energy)
        return
    elif idx > n:  # 최종 돌 넘어가면 리턴
        return
    if use_big_jump == False:  # 매우 큰 점프 사용
        dfs(idx + 3, True, energy + k)
    dfs(idx + 1, use_big_jump, energy + stones[idx][0])  # 작은 점프
    dfs(idx + 2, use_big_jump, energy + stones[idx][1])


dfs(1, False, 0)
print(min(arr))
