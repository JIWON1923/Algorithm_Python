while True:
    string = input()
    if string == '0': break
    print('yes') if ''.join(reversed(string)) == string else print('no')