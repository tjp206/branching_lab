

def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return sorted(scores, reverse=True)[0:3]
    

def high_to_low(scores):
    return sorted(scores, reverse=True)


# I havd been working on this problem, it is now ready for merge to master.