def get_gcd(a, b):
    while min(a, b):
        tmp = max(a, b) % min(a, b)
        a, b = tmp, min(a, b)
    return b


a, b = map(int, input().split())
gcd = get_gcd(a, b)
lcm = a*b // gcd
print(gcd)
print(lcm)