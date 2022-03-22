import sys
n = int(sys.stdin.readline())
numbers, cnt = [], {}
for i in range(n):
    num = int(sys.stdin.readline())
    cnt[num] = cnt[num] + 1 if num in cnt else 1
    numbers.append(num)
numbers.sort()
print(round(sum(numbers) / n)) # average
print(numbers[n//2:n//2+1][0]) # 중간값
mode = sorted([k for k,v in cnt.items() if max(cnt.values()) == v])
print(mode[0] if len(mode) == 1 else  mode[1])
print(abs(numbers[-1] - numbers[0]))