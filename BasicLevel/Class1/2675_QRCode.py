test = int(input())
for i in range(test):
    num, code = input().split()
    for j in code:
        print(j*int(num), end="")
    print()