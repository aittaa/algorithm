


def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    answer = dict()

    for i in range(len(steps_one)):
        answer[names_one[i]] = steps_one[i]
    
    for i in range(len(steps_two)):
        if names_two[i] in answer:
            answer[names_two[i]] += steps_two[i]
        else:
            answer[names_two[i]] = steps_two[i]
    
    for i in range(len(steps_three)):
        if names_three[i] in answer:
            answer[names_three[i]] += steps_three[i]
        else:
            answer[names_three[i]] = steps_three[i]
    
    answer2 = list(answer.items())
    answer2.sort(key = lambda x : (x[1], x[0]), reverse=True)

    result = []

    for i in range(len(answer2)):
        result.append(answer2[i][0])



    return result