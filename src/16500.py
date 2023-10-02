# 문자열 판별

'''
S를 A에 포함된 문자열을 공백없이 붙여서 만들 수 있는지 없는지 구하는 프로그램
'''

import sys
input = sys.stdin.readline

s = list(input().rstrip())
n = int(input())
dp = [0] * (len(s) + 1)
dp[0] = 1

words = [input().rstrip() for _ in range(n)]

for i in range(len(s) + 1):
  for word in words:
    word_len = len(word)
    if i >= word_len and dp[i - word_len] == 1 and s[i - word_len:i] == list(word):
      dp[i] = 1

print(1) if dp[len(s)] else print(0)