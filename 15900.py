import sys
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
for i in range(n-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

stack = [[1, 0]]
check = [0] * (n+1)
check[1] = -1

li = []

while stack:
    cn, l = stack.pop()
    check[cn] = 1

    if cn != 1 and len(tree[cn]) == 1:
        li.append(l)
        continue

    for nn in tree[cn]:
        if check[nn] == 0:
            stack.append([nn, l+1])

sum_li = sum(li)

if sum_li % 2:
    print('Yes')
else:
    print('No')
