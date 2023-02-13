def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        return False
    return s.isdigit()


print(solution("1223"))
