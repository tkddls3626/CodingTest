def solution ():
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    answer = []

    cmd_length = len(commands)
    for i in range(cmd_length):

        arr_list = array[commands[i][0]-1:commands[i][1]]

        arr_list.sort()

        answer.append(arr_list[commands[i][2]-1])
        print(i)
        print(answer)
    return answer
print(solution())