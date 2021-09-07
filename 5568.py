# import sys
# import itertools


# def d():
#     return int(sys.stdin.readline())


# n = d()
# case = d()
# li = []
# for _ in range(n):
#     li.append(str(d()))
# comb = list(itertools.permutations(li, case))
# numbers = set(map(''.join, comb))

# print(len(numbers))


def dfs(depth):
    if depth == k:
        s.add(''.join(map(str, li)))
        return
    for i in range(n):
        if check[i]:
            continue
        li.append(nums[i])
        check[i] = 1
        dfs(depth+1)
        li.pop()
        check[i] = 0


n, k = int(input()), int(input())
nums = [int(input()) for _ in range(n)]
li, s = [], set()
check = [0]*n
dfs(0)
print(s)
