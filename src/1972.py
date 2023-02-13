import sys
input = sys.stdin.readline

while True:
    str = input().rstrip()
    if str[0] == '*':
        break

    flag = True
    for i in range(1, len(str)):
        li = []
        for j in range(len(str) - i):
            li.append(str[j] + str[j+i])
        for k in range(len(li) - 1):
            if li[k] in li[k + 1:]:
                flag = False

    if flag:
        print(f"{str} is surprising.")
    else:
        print(f"{str} is NOT surprising.")
