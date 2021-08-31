n = int(input())
time_list = list(map(int, input().split()))
result = 0
time_list.sort(reverse=True)
for time in range(len(time_list)):
    result += (time+1) * time_list[time]
print(result)