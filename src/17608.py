import sys
N = int(sys.stdin.readline())

li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))

# li.reverse()
cnt = 0
# N = li[0]
N = li[-1]
for i in li[::-1]:
    print(i)
    if i > N:
        cnt += 1
        N = i
print(cnt+1)