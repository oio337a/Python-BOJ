# from collections import deque
# DFS

# def solution(board):
#     n = len(board)
#     answer = int(1e9)
#     dp = [[int(1e9) for _ in range(n)] for _ in range(n)]
#     # 현재 지나간 길을 확인하기 위한 idx 추가
#     directions = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]
#     # i, j, cost, direction
#     q = deque([(0, 0, 0, -1)])
#     while q:
#         i, j, cost, dir_idx = q.popleft()
#         # 정답 범위이고, 현재 cost가 더 적을 때 값 할당
#         if (i, j) == (n - 1, n - 1) and answer > cost:
#             answer = cost
#         for direction in directions:
#             # 다음 값 셋팅
#             next_i = i + direction[0]
#             next_j = j + direction[1]
#             add_cost = 1 if dir_idx == direction[2] or dir_idx == -1 else 6
#             # 현재 값 판단할 지 여부
#             if not (0 <= next_i < n and 0 <= next_j < n) or board[next_i][next_j] == 1:
#                 continue
#             if dp[next_i][next_j] < cost + add_cost:
#                 continue
#             # dp에 값 설정 및 큐에 추가
#             dp[next_i][next_j] = cost + add_cost
#             q.append((next_i, next_j, cost + add_cost, direction[2]))
#     return answer * 100


# solution()


# n = "X.XXXXX.X."


# def solution(S):
#     enable_print = S % 10
#     while S > 0:
#         if enable_print >= 0:
#             enable_print = 1
#         if enable_print == 1:
#             print(S % 10, end="")
#         S = S // 10


# def solution(S):
#     cnt = 0
#     num = len(S) - 1
#     S = list(S)
#     while num >= 0:
#         if S[num] == "X":
#             cnt += 1
#             num -= 3
#         else:
#             num -= 1
#     print(cnt)


# solution(n)


# # 매일 1일1커밋 하기 생활화!!

# nums = [0,1,0,3,12]

# count = nums.count(0)
# # nums[:] = [i for i in nums if i != 0]
# random = [i for i in nums if i != 0]
# nums = random
# nums += [0] * count

# print(nums)

def solution(survey, choices):
    answer = ''
    dic= {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }
    
    for s,c in zip(survey,choices):
        if c>4:     dic[s[1]] += c-4
        elif c<4:   dic[s[0]] += 4-c
    
    li = list(dic.items())
    
    for i in range(0,8,2):
        if li[i][1] < li[i+1][1]: answer += li[i+1][0]
        else:   answer += li[i][0]
        
    return answer