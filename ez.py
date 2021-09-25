# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# a = []
# report.sort()
# for i in report:
#     a.append(i.split())
# dic = {f'{i}': 0 for i in id_list}
# id_list_1 = [[i] for i in id_list]
# for i in a:
#     dic[i[1]] += 1

# # for i in a:
# #     if i[0] in id_list_1:

# print(id_list_1[0][0])
# # print(a)

# n = 437674
# q = 3
# rev_base = ''

# while n > 0:
#     n, mod = divmod(n, q)
#     rev_base += str(mod)
#     a = rev_base[::-1]

# count = 0
# for i in range(len(a)):
#     if a[i] == '0':
#         count = 2
#     else:
#         count = 1


# def solution(n, q):
#     rev_base = ''

#     while n > 0:
#         n, mod = divmod(n, q)
#         rev_base += str(mod)
#         a = rev_base[::-1]

#     count = 0
#     for i in range(len(a)):
#         print(type(a[i]))
#         if a[i] == 0:
#             count += 2
#         else:
#             count += 1
#     return count


# print(solution(n, q))

# skill = [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]
# board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in skill:
#     if i[0] == 1:
#         for j in range(i[1], i[4]+1):
#             for k in range(i[2], i[3]+1):
#                 board[j][k] -= i[-1]
#     else:
#         for j in range(i[1], i[4]+1):
#             for k in range(i[2], i[3]+1):
#                 board[j][k] += i[-1]
# print(board)

for i in range(2, 1):
    print(i)
