def solution():
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
# lambda = 매게변수 x를 받고 정렬한다음 배열 인덱스 -1을 해준다음  반복을 해준다
print(solution())