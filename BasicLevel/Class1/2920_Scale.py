import sys
scale = list(map(int, sys.stdin.readline().split()))
result = 1
for i in range(len(scale)-1):
    if scale[i] > scale[i+1] :
        if scale[i] - scale[i+1] != 1: result *= 0
        else: result *= 1
    elif scale[i] < scale[i+1]:
        if scale[i] - scale[i+1] != -1: result *= 0
        else: result *= -1
if result == -1: print('ascending')
elif result == 1: print('descending')
else: print('mixed')
