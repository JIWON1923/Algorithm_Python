def solution(participant, completion):
    if len(set(participant)) != len(set(completion)):
        winner = list(set(participant) - set(completion))
        return winner[0]
    else:
        participant.sort()
        completion.sort()
        for i in range(len(completion)):
            if participant[i] != completion[i]:
                return participant[i]
        return participant[-1]


"""
# 시간 초과 오류 (효율성테스트 5번 문제 틀림) => 90
def solution(participant, completion):
    if len(set(participant)) != len(set(completion)):
        winner = list(set(participant) - set(completion))
        return winner[0]
    else:
        for person in participant:
            if person in completion:
                print(2)
                completion.remove(person)
            else:
                print(3)
                return person
"""