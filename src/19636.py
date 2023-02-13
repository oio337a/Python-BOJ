# 체중은 (일일 에너지 섭취량 − 일일 에너지 소비량) g/Kcal만큼 더해진다
# 일일 에너지 소비량은 일일 기초 대사량과 일일 활동 대사량을 더한 값이다.
# (일일 에너지 섭취량 − 일일 에너지 소비량) 의 절댓값이 기초 대사량 변화 역치 T Kcal 초과라면, 일일 기초 대사량은 ⌊ (일일 에너지 섭취량 − 일일 에너지 소비량) / 2 ⌋ 만큼 더해진다

"""
체중, 에너지 섭취량은 한번만 변함.
W += E - (I + A)
"""
# # W 체중, I 기초대사량, T 역치
W, I, T = map(int, input().split())
# # D 기간, E 에너지 섭취량, A 활동대사량
D, E, A = map(int, input().split())

answer1 = 0
answer2 = 0

w1 = w2 = W
i1 = i2 = I

for _ in range(D):
    w1 += E-(i1+A)
    w2 += E-(i2+A)

    if abs(E-(i2+A)) > T:
        i2 += (E-(i2+A))//2
    if w1 <= 0 or i1 <= 0:
        answer1 = 1
    if w2 <= 0 or i2 <= 0:
        answer2 = 1
if answer1 == 0:
    print(w1, i1)
else:
    print("Danger Diet")
if answer2 == 0:
    print(w2, i2, end=" ")

    if I-i2 > 0:
        print("YOYO")
    else:
        print("NO")
else:
    print("Danger Diet")
