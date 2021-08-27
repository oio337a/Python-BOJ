li = list(map(str, input().split()))

# for i in range(len(li)):
#     for j in range(1, len(li)):
#         if li[j-1] > li[j]:
#             temp = li[j-1]
#             li[j-1] = li[j]
#             li[j] = temp
#             for _ in li:
#                 if _ == li[-1]:
#                     print(li[-1])
#                 else:
#                     print(li[_], end=' ')


for j in range(len(li)):
    for i in range(1, len(li)):
        if li[i] < li[i-1]:
            li[i], li[i-1] = li[i-1], li[i]
            print(' '.join(li))
