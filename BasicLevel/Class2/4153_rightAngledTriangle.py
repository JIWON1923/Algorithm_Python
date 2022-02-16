import sys
while True:
    legs = list(map(int, (sys.stdin.readline().split())))
    legs.sort()
    if legs[2] == 0: break
    print("right") if legs[0]**2 + legs[1]**2 == legs[2]**2 else print("wrong")