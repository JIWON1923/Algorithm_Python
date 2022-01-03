month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
def solution(a, b):
    return week[(sum(month[0:a-1]) + b)%7-1]