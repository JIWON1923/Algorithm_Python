def solution(sizes):
    sizes = [sorted(i) for i in sizes]
    a = max(sizes, key=lambda x:x[0])
    b = max(sizes, key=lambda x:x[1])
    return a[0] * b[1]