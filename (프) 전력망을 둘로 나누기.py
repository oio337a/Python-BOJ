
def dfs(s, visit):
    global count
    visit.append(s)
    count += 1
    for i in dic[s]:
        if i not in visit:
            dfs(i, visit)


def solution(n, wires):
    global dic, count
    res = []
    dic = {}

    # tree 연결하기
    for i in range(n):
        dic[i+1] = set()
    for a, b in wires:
        dic[a].add(b)
        dic[b].add(a)

    # 모든 경우의 수 확인 (간선 1개씩 제거하고 카운트 해보기)
    for a, b in wires:
        dic[a].remove(b)
        dic[b].remove(a)
        count = 0
        dfs(1, [])
        res.append(abs(n - (count * 2)))
        dic[a].add(b)
        dic[b].add(a)

    return min(res)


# print(solution(9, [[3, 1], [3, 2], [4, 3], [
#       4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
