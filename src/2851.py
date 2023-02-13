import sys

li = []
num = 0
for i in range(10):
    li.append(int(sys.stdin.readline()))
for j in li:
    num += j
    if num >= 100:
        if num - 100 > 100 - (num - j):
            num -= j
        break
print(num)
