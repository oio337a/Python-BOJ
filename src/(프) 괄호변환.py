def check(p):
    stack = []
    stack.append(p[0])
    for i in range(1, len(p)):
        if len(stack) == 0 or stack[-1] == ')' or (stack[-1] == '(' and p[i] == '('):
            stack.append(p[i])
        else:
            stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False


def solution(p):
    global answer
    answer = ''
    l, r = 0, 0  # l = '(' r = ')'
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            if check(p[:i]):
                answer += p[:i] + solution(p[i:])
            else:
                answer += '('
                for i in p[1:-1]:
                    answer += ')' if i == '(' else '('
                answer += ')'
    return answer


print(solution("(()())()"))
