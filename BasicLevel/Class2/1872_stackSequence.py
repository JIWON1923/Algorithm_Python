"""
n, stack, sequence

1. n, sequence 입력받기
2. stack에 넣어가며 만들 수 있는지 확인
    - Sequence[i]까지 차례대로 삽입
    - stack[-1]보다 sequence[i]가 작으면 pop
    - pop했는데, 해당 원소가 아니면 NO 출력
"""

n = int(input())
sequence, stack, value, result = [], [], 0, ""
for i in range(n):
    num = int(input())
    if i == 0:
        stack = [i for i in range(1, num+1)]
        value = num
        result += "+" * stack[-1]
        stack.pop(-1)
        result += "-"

    else:
        if len(stack) != 0:
            if stack[-1] < num:
                for j in range(value+1, num+1):
                    stack.append(j)
                    result += "+"
                stack.pop(-1)
                result += "-"
                value = num
            elif stack[-1] == num:
                stack.pop(-1)
                result += "-"
            else:
                break
        else:
            for j in range(value+1, num+1):
                stack.append(j)
                result += "+"
            stack.pop(-1)
            result += '-'
            value = num
print('\n'.join(result)) if len(stack) == 0 else print("NO")



