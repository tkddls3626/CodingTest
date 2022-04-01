def solution():
    participant=["leo", "kiki", "eden"]
    comlpetion=["eden", "kiki"]
    tmp = 0
    dic = {}

    for p in participant:
        dic[hash(p)] = p

        tmp += int(hash(p))

    for com in comlpetion:

        tmp -= int(hash(com))

    return dic[tmp]

print(solution())