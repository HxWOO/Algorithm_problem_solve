n = int(input())
score_list = list(map(int, input().split()))


def fake(x):
    return x/max(score_list)*100


score_list = list(map(fake, score_list))
print(sum(score_list)/n)
