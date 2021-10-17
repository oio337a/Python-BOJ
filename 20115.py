"""
가장 많은 양에 그 다음으로 많은양의 절반을 넣으면 된다. 
"""
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

li.sort(reverse=True)
answer = li[0]

for i in range(1, n):
    answer += li[i]/2

print('%g' % answer)
