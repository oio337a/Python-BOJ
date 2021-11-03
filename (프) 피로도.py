# """
# 최소 피로도, 소모 피로도

# 던전을 최대한 많이 탐험

# 던전 최대 8!
# """

# from itertools import permutations


# def solution(k, dungeons):
#     answer = []

#     per = list(permutations(dungeons, len(dungeons)))

#     for i in per:
#         count = 0
#         piro = k
#         for j in range(len(i)):
#             if piro >= i[j][0]:
#                 piro -= i[j][1]
#                 count += 1
#         answer.append(count)
#     return max(answer)


# solution(80, [[80, 20], [50, 40], [30, 10]])


def solution(k, dungeons):
    # [False, False, False]
    visited = [False] * len(dungeons)
    dfs(k, visited, dungeons, 0)
    global result
    return result


result = 0
# depth -> k 를 의미 , 유저의 현재 피로도


def dfs(depth, visited, dungeons, count):
    global result
    result = max(result, count)

    for i in range(len(dungeons)):
        if visited[i] is False:
            if depth >= dungeons[i][0]:
                visited[i] = True
                depth = depth - dungeons[i][1]
                dfs(depth, visited, dungeons, count+1)
                depth = depth + dungeons[i][1]
                visited[i] = False


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
