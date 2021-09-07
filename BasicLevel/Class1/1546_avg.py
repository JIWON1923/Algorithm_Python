import sys
num = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
score.sort(reverse=True)
max_value = score[0]

for index, value in enumerate(score):
    score[index] = value/max_value*100
print(sum(score)/num)