n, m = map(int, input().split())
check = [0] * n
soon_li = []  # 순열 담을 리스트


def solve(d, n, m):
    if d == m:
        print(' '.join(map(str, soon_li)))
        return
    for i in range(len(check)):
        if not check[i]:
            check[i] = 1
            soon_li.append(i+1)
            solve(d+1, n, m)
            check[i] = 0
            soon_li.pop()


solve(0, n, m)

# from itertools import permutations
# n, m = map(int, input().split())
# p = permutations(range(1, n+1), m)

# for i in p:
#     print(' '.join(map(str, i)))
