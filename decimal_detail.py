# 입력받은 숫자가 소수인지 반펼
# 소수:TRUE , 소수X:FALSE
import math
from itertools import permutations

def numberCheck(num):
    #0,1 은 소수가 아님
    if num == 0 or num == 1:
        return False
    else:
        # 2부터 입력받은 숫자의 제곱값까지 반복
        # 입력받은 값이 10이면 10의제곱까지 반복 총(100번)
        # 그러나 100은 2의 배수로 반복 1번하고 종료됨
        for i in range(2, int(math.sqrt(num)) + 1):
            #print(i)
            #입력받은 값이 2부터 시작해서 나워 떨어지는지 체크
            if num % i == 0:
                return False
    return True
def solution(numbers):
    answer = []
    # 숫자의 길이 만큼 반복하기
    for i in range(1, len(numbers)+1):
        arr = list(permutations(numbers, i))
        #모든 경우의 수를 반복하기
        for j in range(len(arr)):
            # 문자를 숫자로 변환하기 011 => 11로 변경
            num = int(''.join(map(str,arr[j])))
            print("num :" , num)
            #소수인지 확인 - 에라토스테네스의 채 응용
            if numberCheck(num):
                # 소수이면 정답에 저장
                answer.append(num)
    # 중복된 경우의 수가 나올 수 있어 set 데이터 구조로 중복을 제거
    answer =set(answer)
    # set 구조의 숫자 계산
    return len(answer)