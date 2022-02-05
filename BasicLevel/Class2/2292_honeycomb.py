n = int(input())
numbers = 1
for i in range(0, n+1):
    numbers = numbers + 6*i
    if numbers >= n:
        print(i+1)
        break
