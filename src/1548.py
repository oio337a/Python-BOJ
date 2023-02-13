"""
삼각관계를 만족하는 수열은 몇
"""

import sys
input = sys.stdin.readline

n = int(input())
li = [map(int, input().split())]

if len(li) <= 3:
    if li[0] + li[1] < li[2]:
        pass
else:
    pass
