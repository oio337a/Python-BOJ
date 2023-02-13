import sys

name = list(map(str, sys.stdin.readline().strip()))
answer = ''
temp = ''
name_count = [0]*26
odd = 0
for i in name:
    name_count[ord(i)-65] += 1

for i in range(26):
    if name_count[i] % 2 == 1:
        odd += 1
        temp = chr(i+65)
    answer += chr(i+65) * (name_count[i] // 2)

reverse_answer = list(answer)
reverse_answer.reverse()
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer + temp + ''.join(map(str, reverse_answer)))
"""
문자열 insert 와 remove 사용한 방법.. 실패!!
s = list(input())

li = []
x = []
if len(s) % 2 == 1:
    for i in range(len(s)//2+1):
        if s[i] in s[i+1:]:
            li.insert(i, s[i])
            li.insert(-i, s[i])
            s.remove(s[i])
        else:
            x.append(s[i])

    if len(x) <= 1:
        li.insert(len(li)//2, x[0])
        print(''.join(li))
    else:
        print("I'm Sorry Hansoo")
else:
    for i in range(len(s)//2):
        if s[i] in s[i+1:]:
            li.insert(i, s[i])
            li.insert(-i-1, s[i])
            print(i, 'i')
            s.remove(s[s.index(s[i])])
            print(li)
        else:
            x.append(s[i])
    print(x, 'x')
    if len(x) == 1:
        li.insert(len(li)//2, x[0])
        print(''.join(li))
    elif len(x) == 0:
        print(''.join(li))
    else:
        print("I'm Sorry Hansoo")
"""
