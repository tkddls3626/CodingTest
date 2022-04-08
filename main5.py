def solution():
    numbers = [6,10,2]

    print(type(numbers))
    print(type(numbers[0]))

    numbers = list(map(str, numbers))

    print(type(numbers))
    print(type(numbers[0]))

    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))
print(solution())