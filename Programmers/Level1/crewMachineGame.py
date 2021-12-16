def solution(board, moves):
    stack = []
    answer = 0
    crews = select_crew(board)
    print(crews)

    for move in moves:
        if not crews[move - 1]:
            continue
        crew = crews[move - 1][0]
        if len(stack) == 0:
            stack.append(crew)
        elif stack[-1] == crew:
            answer += 2
            del stack[-1]
        else:
            stack.append(crew)
        del crews[move - 1][0]
    return answer


def select_crew(table):
    crews = []
    for i in range(len(table)):
        crews.append([])
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != 0:
                crews[j].append(table[i][j])
    return crews