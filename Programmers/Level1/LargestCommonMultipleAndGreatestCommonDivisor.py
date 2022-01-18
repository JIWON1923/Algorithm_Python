def get_gcd(n,m):
    tmp = min(n, m)
    while tmp:
        tmp = max(n, m) % min(n, m)
        n, m = tmp, min(n, m)
    return m


def solution(n, m):
    gcd = get_gcd(n, m)
    lcm = n * m / gcd
    return [gcd, lcm]