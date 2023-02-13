import sys
input = sys.stdin.readline

n = int(input())

answer = 0
enter, out = dict(), []
for i in range(n):
    car = input()
    enter[car] = i
for j in range(n):
    car = input()
    out.append(car)

for i in range(n-1):  # 2
    for j in range(i+1, n):  # 3
        if enter[out[i]] > enter[out[j]]:  # 나온차의 차량 번호를 가지고 딕셔너리의 밸류값을 비교해서 다르다면, +1
            answer += 1
            break
print(answer)
