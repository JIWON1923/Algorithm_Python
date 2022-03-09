def solution(numbers, hand):
    answer = ''
    left, right = 10, 12
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left = num
        elif num in [3, 6, 9]:
            answer += "R"
            right = num
        else:
            num = 11 if num == 0 else num
            if sum(divmod(abs(left-num), 3)) > sum(divmod(abs(right-num), 3)):
                answer += "R"
                right = num
            elif sum(divmod(abs(left-num), 3)) == sum(divmod(abs(right-num), 3)):
                if hand == "left":
                    answer += "L"
                    left = num
                else:
                    answer += "R"
                    right = num
            else:
                answer += "L"
                left = num
    return answer