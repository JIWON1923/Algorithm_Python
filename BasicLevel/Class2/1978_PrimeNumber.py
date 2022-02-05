n = int(input())
numbers = set(map(int, input().split()))
max_value = max(numbers)

number = set(range(2, max_value+1))
for i in range(2, max_value+1):
    if i in number:
        number -= set(range(2*i, max_value+1, i))
print(len(number&numbers))