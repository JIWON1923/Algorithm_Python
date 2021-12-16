useable_symbol = ['-', '_', '.']
remove = []


def solution(new_id):
    new_id = new_id.lower() # 1단계

    temp = new_id
    for i in range(len(new_id)): #2단계
        if not new_id[i].isalnum():
            if not (new_id[i] in useable_symbol):
                temp = temp.replace(new_id[i], "")
    new_id = temp

    cnt = new_id.count('..')
    for i in range(cnt): # 3단계
        new_id = new_id.replace('..', '.')
    new_id = new_id.strip('.') # 4단계

    if new_id == "" : new_id = "a" # 5단계

    new_id = new_id[:15] # 6단계
    new_id = new_id.strip('.')

    if len(new_id) < 3:
        new_id = new_id + new_id[-1]*(3-len(new_id))
    return new_id