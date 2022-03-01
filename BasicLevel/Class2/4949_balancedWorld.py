while 1:
    check = input()
    if check == '.': break
    stack = []
    result = True
    for i in check:
        if i == '[' or i == '(':
            stack.append(i)
        if i == ']' or i == ')':
            if len(stack) == 0:
                result = False
                break
            c = stack.pop(-1)
            if i == ']' and c != '[':
                result = False
                break
            if i == ')' and c != '(':
                result = False
                break
    if result and not len(stack):
        print('yes')
    else:
        print('no')