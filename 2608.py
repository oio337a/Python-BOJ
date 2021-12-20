import sys
input = sys.stdin.readline

'''
1. 보통 큰 숫자를 왼쪽에 작은 숫자를 오른쪽에 쓴다. 
2. V, L, D는 한 번만 사용할 수 있고 I, X, C, M은 연속해서 세 번까지만 사용할 수 있다.
3. IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900
    3-1. 이들 각각은 한 번씩만 사용할 수 있다. 
    3-2.  IV 와 IX 는 같이 쓸 수 없으며 XL 과 XC, CD 와 CM 또한 같이 쓸 수 없다.

I V  X  L  C   D    M
1 5 10 50 100 500 1000
'''

first = list(input().rstrip())
second = list(input().rstrip())

su_1 = 0
su_2 = 0
flag = True
for i in range(len(first)):
    if flag:
        if first[i] == 'M':
            su_1 += 1000
        elif first[i] == 'D':
            su_1 += 500
        elif first[i] == 'C':
            if i != len(first)-1:
                if first[i+1] == 'D':
                    su_1 += 400
                    flag = False
                    continue
                elif first[i+1] == 'M':
                    su_1 += 900
                    flag = False
                    continue
            su_1 += 100
        elif first[i] == 'L':
            su_1 += 50
        elif first[i] == 'X':
            if i != len(first)-1:
                if first[i+1] == 'L':
                    su_1 += 40
                    flag = False
                    continue
                elif first[i+1] == 'C':
                    su_1 += 90
                    flag = False
                    continue
            su_1 += 10
        elif first[i] == 'V':
            su_1 += 5
        elif first[i] == 'I':
            if i != len(first)-1:
                if first[i+1] == 'V':
                    su_1 += 4
                    flag = False
                    continue
                elif first[i+1] == 'X':
                    su_1 += 9
                    flag = False
                    continue
            su_1 += 1
    else:
        flag = True


for i in range(len(second)):
    if flag:
        if second[i] == 'M':
            su_2 += 1000
        elif second[i] == 'D':
            su_2 += 500
        elif second[i] == 'C':
            if i != len(second)-1:
                if second[i+1] == 'D':
                    su_2 += 400
                    flag = False
                    continue
                elif second[i+1] == 'M':
                    su_2 += 900
                    flag = False
                    continue
            su_2 += 100
        elif second[i] == 'L':
            su_2 += 50
        elif second[i] == 'X':
            if i != len(second)-1:
                if second[i+1] == 'L':
                    su_2 += 40
                    flag = False
                    continue
                elif second[i+1] == 'C':
                    su_2 += 90
                    flag = False
                    continue
            su_2 += 10
        elif second[i] == 'V':
            su_2 += 5
        elif second[i] == 'I':
            if i != len(second)-1:
                if second[i+1] == 'V':
                    su_2 += 4
                    flag = False
                    continue
                elif second[i+1] == 'X':
                    su_2 += 9
                    flag = False
                    continue
            su_2 += 1
    else:
        flag = True
num = su_1 + su_2
print(num)

ans = ''
su = str(num)
t = len(su)
n = len(su)
while n:
    num = int(su[t-n])
    if n == 4:
        ans += 'M'*num
    elif n == 3:
        if num == 9:
            ans += 'CM'
        elif num == 4:
            ans += 'CD'
        else:
            if num >= 5:
                ans += 'D'
            ans += 'C'*(num % 5)
    elif n == 2:
        if num == 9:
            ans += 'XC'
        elif num == 4:
            ans += 'XL'
        else:
            if num >= 5:
                ans += 'L'
            ans += 'X'*(num % 5)
    elif n == 1:
        if num == 9:
            ans += 'IX'
        elif num == 4:
            ans += 'IV'
        else:
            if num >= 5:
                ans += 'V'
            ans += 'I'*(num % 5)
    n -= 1
print(ans)
