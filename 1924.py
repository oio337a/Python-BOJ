x, y = map(int, input().split())

day = 0
mon_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i in range(x-1):
    day += mon_list[i]
day = (day + y) % 7

print(week_list[day])
