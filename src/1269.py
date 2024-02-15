
# import sys

# input = sys.stdin.readline

# a, b = map(int, input().split())

# li_1 = set(list(map(int, input().split())))
# li_2 = set(list(map(int, input().split())))

# answer_1 = li_1 - li_2
# answer_2 = li_2 - li_1

# print(len(answer_1)+len(answer_2))

import sys
from collections import Counter
input = sys.stdin.readline

a, b = map(int, input().split())
l = list(map(int, input().split()))
l += map(int, input().split())
cnt = Counter(l)

ans = 0
for i in cnt:
  if cnt[i] == 1:
    ans += 1

print(ans)