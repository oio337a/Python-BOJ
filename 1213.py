name_count = [0 for _ in range(26)]

print(name_count)
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
