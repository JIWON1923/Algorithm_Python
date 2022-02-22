def solution(s):
    word = s.lower().split(' ')
    result = ''
    for i in word:
        result += i + ' ' if not i[0].isalpha() else i[0].upper() + i[1:] +' '
    return result[:-1]