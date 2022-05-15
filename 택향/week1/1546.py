subject_cnt = int(input())
score_list = list(map(int, input().split(' ')))


def solution():
    M = max(score_list)
    new_score_list = list()

    for score in score_list:
        new_score = (score / M) * 100
        new_score_list.append(new_score)

    med = sum(new_score_list) / len(new_score_list)
    return med


print(solution())
