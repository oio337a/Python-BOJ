hour, minute = map(int, input().split())

60 - 10 - 35
if minute < 45:
    minute = 60 - (45-minute)
    hour -= 1
else:
    minute -= 45
if hour == -1:
    hour = 23
print(hour, minute)
