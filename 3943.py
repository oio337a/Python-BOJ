import sys

for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    li = []
    while True:
        if 1 in li:
            break
        li.append(a)
        if a % 2 == 0:
            a //= 2
        else:
            a = a*3+1
    print(max(li))
