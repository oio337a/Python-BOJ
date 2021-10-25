# # BFS
# def solution(numbers, target):
#     answer = 0
#     leaves = [0]
#     for num in numbers:
#         tmp = []
#         for parent in leaves:
#             tmp.append(parent + num)
#             tmp.append(parent - num)
#         leaves = tmp
#     for leaf in leaves:
#         if leaf == target:
#             answer += 1
#     return answer


# DFS
def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer


def dfs(numbers, target, d):
    answer = 0
    if d == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += dfs(numbers, target, d+1)
        numbers[d] *= -1
        answer += dfs(numbers, target, d+1)
        return answer
