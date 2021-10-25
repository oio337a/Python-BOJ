def solution(record):
    answer = []
    user_date = dict()
    actions = []

    for i in record:
        info = i.split()
        action, user_id = info[0], info[1]
        if action in ("Enter", "Change"):
            user_date[user_id] = info[2]
        actions.append((action, user_id))

    for i in actions:
        action, user_id = i[0], i[1]
        if action == 'Enter':
            answer.append(f'{user_date[user_id]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{user_date[user_id]}님이 나갔습니다.')
    return answer
