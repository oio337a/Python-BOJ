# 부분배열 고르기

import sys
input = sys.stdin.readline


# 스택 활용
n, data = int(input()), list(map(int, input().split())) + [0]

pre_sum = [0]
for i in range(n):
  pre_sum.append(pre_sum[-1]+data[i])

stack, result = [], 0
for i in range(n + 1):
  h = data[i]
  j = i
  while stack and stack[-1][0] >= h:
    h1, j = stack.pop()
    result = max(result, (pre_sum[i] - pre_sum[j]) * h1)
  stack.append((h, j))
print(result)

# 분할정복

def solve(s, e):
    if s == e:
        return A[s] * A[s]
    mid = (s+e)//2
    ret = max(solve(s, mid), solve(mid+1, e))

    left = mid
    right = mid + 1
    _sum = A[left] + A[right]
    min_val = min(A[left], A[right])
    ret = max(ret, min_val * _sum)
    while left > s or right < e:
        if right < e and (left == s or A[left-1] < A[right + 1]):
            right += 1
            _sum += A[right]
            min_val = min(min_val, A[right])
        else:
            left -= 1
            _sum += A[left]
            min_val = min(min_val, A[left])
        ret = max(ret, min_val * _sum)
    return ret

n = int(input())
A = list(map(int, input().split()))
print(solve(0, n-1))

