import sys
def calculate(score):
    result, check = 0, 0
    for i in range(len(score)):
        if score[i] == 'O':
            check += 1
            result += check
        elif score[i] == 'X': check = 0
    print(result)

case = int(sys.stdin.readline())
for i in range(case):
    score = list(sys.stdin.readline())
    calculate(score)
