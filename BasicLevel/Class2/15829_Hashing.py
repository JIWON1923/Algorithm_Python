result = 0
l = int(input())
num = input()
for i in range(l):
    result += (ord(num[i])-96)*(31**i)
print(result%1234567891)