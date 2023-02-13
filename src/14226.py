from collections import deque

n = int(input())
q = deque()
q.append((1, 0))  # 현재 이모티콘 개수, 클립보드 이모티콘 개수
visited = dict()
visited[(1, 0)] = 0

while q:
    s, c = q.popleft()
    if s == n:
        print(visited[(s, c)])
        break

    # 1번 : 이모티콘 복사
    if (s, s) not in visited.keys():
        visited[(s, s)] = visited[(s, c)] + 1
        q.append((s, s))
    # 2번 : 화면의 이모티콘 삭제
    if (s-1, c) not in visited.keys():
        visited[(s-1, c)] = visited[(s, c)] + 1
        q.append((s-1, c))
    # 3번 : 클립보드 붙여넣기
    if (s+c, c) not in visited.keys():
        visited[(s+c, c)] = visited[(s, c)] + 1
        q.append((s+c, c))