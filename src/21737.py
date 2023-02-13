def cal(num1, num2, op):
    if op == 'S':
        return num1 - num2
    elif op == 'M':
        return num1 * num2
    elif op == 'U':
        return num1//num2 if num1 > 0 else -(abs(num1)//num2)
    elif op == 'P':
        return num1 + num2


N = int(input())
string = input()
answer = ''
temp = ''
opt = ''
out_c = False
for c in string:
    if c.isdigit():
        if opt:
            temp += c
        else:
            answer += c
    else:
        if opt and opt != 'C':
            answer = cal(int(answer), int(temp), opt)
            temp = ''
        if c == 'C':
            out_c = True
            print(int(answer), end=' ')
        opt = c

if not out_c:
    print('NO OUTPUT')
