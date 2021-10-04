def solution(s):
    li = [s.split()]
    for i in li:
        for j in range(len(i)):
            if j % 2 == 0:
                i[j] = chr(ord(i[j]) + 32)
    return


print(solution("try hello world"))
