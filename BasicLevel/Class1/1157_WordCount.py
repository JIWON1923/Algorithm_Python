alphabet = input().upper()
list(alphabet).sort()
set_alphabet = set(alphabet)
max_count = 0
index = 0

for alpha in set_alphabet:
    now = alphabet.count(alpha)
    if max_count < now:
        max_alpha = alpha
        max_count = now
    elif max_count == now: max_alpha = '?'
print(max_alpha)
# 짧게 바꿔야됑