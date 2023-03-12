
from math import ceil

n = int(input())

students = list(map(int, input().split()))

head_monitor_cnt, sub_monitor_cnt = map(int, input().split())

result = n

for student in students:
    student -= head_monitor_cnt
    if student > 0:
      result += ceil(student / sub_monitor_cnt)
print(result)