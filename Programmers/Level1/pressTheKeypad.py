move = [-3, -1, 1, 3]


def solution(numbers, hand):
    left, right = 10, 10
    answer = ''

    for num in numbers:
        if num in [2, 5, 8, 0]:
            tmp = 0
            for i in move:
                if left + i == num:
                    tmp += 1
                if right + i == num:
                    tmp += 2
            if tmp == 3 or 0:
                if hand == "left":
                    left = num
                    answer += "L"
                else:
                    right = num
                    answer += "R"
            elif tmp == 1:
                left = num
                answer += "L"
            elif tmp == 2:
                right = num
                answer += "R"

        elif num in [1, 4, 7]:
            left = num
            answer += "L"
        else:
            right = num
            answer += "R"
    return answer