def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:  # skill_trees의 모든 값을 skill과 비교
        skill_have = []
        flag = True
        for j in range(len(i)):
            if i[j] in skill:  # skill_trees[i][j]의 값이 skill에 있으면 skill_have에 추가
                skill_have.append(i[j])
        for k in range(len(skill_have)):
            if skill_have[k] != skill[k]:  # 순서가 다르면 flag를 False로 변경
                flag = False
                break
        if flag == True:  # 순서가 다 같으면 answer를 +1
            answer += 1

    return answer


# def solution1(skill, skill_trees):
#     answer = 0
#     for skills in skill_trees:
#         skill_list = list(skill)
#         for i in skills:
#             if i in skill:
#                 if i != skill_list.pop(0):  # skill에 포함되는 값이 skill의 첫번째 요소와 일치하는지
#                     break
#         else:  # for - else 문은 break에 걸리지 않고 끝까지 시행됬을때 작동한다
#             answer += 1
#     return answer
