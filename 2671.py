import re


'''
match, search, fullmatch 등을 사용하면 풀수 있는데 
match나 search를 사용하면 10011001 일때 10011로 인식이 되어 
정확한 답을 내놓지 못한다.
'''

s = input()
p = re.compile('(100+1+|01)+')
m = p.fullmatch(s)
if m:
    print("SUBMARINE")
else:
    print("NOISE")
