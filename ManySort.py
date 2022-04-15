def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    results = {1: 0, 2: 0, 3: 0}

    for i in range(len(answers)):

        if student1[i%5] == answers[i]:
            results[1] += 1
        if student2[i%8] == answers[i]:
            results[2] += 1
        if student3[i%10] == answers[i]:
            results[3] += 1
    score = max(results.values())
    answer = []
    for i in range(1,4):
        if results[i] == score:
            answer.append(i)
    return answer