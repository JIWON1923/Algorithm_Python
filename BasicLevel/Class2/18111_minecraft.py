import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
map_dict, result = dict(), []
#result = [] #[시간, 높이]
for i in range(n):
    for j in list(map(int, input().split())):
        map_dict[j] = map_dict[j] + 1 if j in map_dict else 1
for k in range(min(map_dict.keys()), max(map_dict.keys())+1): # k = 기준이 되는 높이
    time, target = 0, b
    for key, value in map_dict.items():
        if key == k: continue
        time = time + (key-k)*value*2 if key > k else time + (k-key) * value
        target = target + (key-k)*value if key > k else target - (k-key) * value
        # if key > k: # 현재 높이 보다 높아 -> 인벤토리에 넣기(2초)
        #     time += ((key - k) * value * 2)
        #     target += ((key - k) * value)
        # elif key < k: # 현재 높이보다 낮아 ->인벤토리에서 빼기(1초)
        #     time += ((k - key) * value)
        #     target -= ((k - key) * value)
    if target >= 0: result.append([time, k])
result.sort(key=lambda x:(x[0], -x[1]))
print(*result[0])