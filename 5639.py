import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

'''입력받기'''
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break
postorder = []

'''재귀(포스트오더, 후위)'''


def postorderset(preorder, left, right):
    if left > right:
        return
    root = preorder[left]
    ls = left + 1
    re = right
    rs = right + 1
    for i in range(right - left + 1):
        if i == 0:
            continue
        if preorder[left + i] > root:  # 루트보다 커지는 첫번째 수, 오른쪽의 시작
            rs = i + left
            break
    le = rs - 1
    postorderset(preorder, ls, le)  # 왼쪽 순환
    postorderset(preorder, rs, re)  # 오른쪽 순환
    postorder.append(root)  # 루트 추가


postorderset(preorder, 0, len(preorder) - 1)
print(*postorder)
