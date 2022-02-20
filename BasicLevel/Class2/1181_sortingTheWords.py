n = int(input())
words = []
for i in range(n):
    words.append(input())
print('\n'.join(sorted(set(words), key=lambda x: [len(x), x])))