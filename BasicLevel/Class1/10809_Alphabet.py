alpha = [-1]*26
word = input()
for index, value in enumerate(word):
    char = ord(value)-ord('a')
    if alpha[char] == -1:
        alpha[char] = index
print(' '.join(repr(i)for i in alpha))