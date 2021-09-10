import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

count = 0
for i in range(97, 123):
    count += abs(a.count(chr(i))-b.count(chr(i)))
print(count)
