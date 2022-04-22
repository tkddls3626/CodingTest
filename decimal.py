import math
# 순서대로 정렬되어있다고 가정!
j = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# 최대값
max_j = max(j)
print ("max_j : " , max_j)
# 소수를 구한 숫자만큼 반복
for i in j:
    # 비교 숫자의 제곱근(루트)과 최대값이 작은 경우에만 소수 찾기 진행
    if math.sqrt(i) < max_j:
        # 배수 삭제를 위해 전체 반복
        for k in j:
            # 자기 자신을 제외하고, 배수인 항목제거
            if k>i and k%i == 0:
                print("i :", i, "/k:", k)
                # 값 삭제하기
                j.remove(k)
print(j)