def solution(price, money, count):
    money = sum([price*i for i in range(1, count+1)]) - money
    return money if money > 0 else 0