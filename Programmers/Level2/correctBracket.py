def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(1)
        else:
            if not len(stack): return False
            stack.pop()

    return True if not len(stack) else False