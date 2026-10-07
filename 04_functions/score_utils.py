def calculate_total(scores):
    s = 0
    for i in scores:
        s = s + i

    return s


def calculate_average(scores):
    s = x = 0

    if not scores:
        return None
        
    for i in scores:
        s = s + i
        x+=1
    avg = s / x

    return avg


def get_highest_score(scores):
    maximum = scores[0]
    for i in scores:
        if i > maximum:
            maximum = i

    return maximum


def get_lowest_score(scores):
    lowest = scores[0]
    for i in scores:
        if i < lowest:
            lowest = i

    return lowest


def count_passing(scores):
    number = index = 0
    for i in scores:
        if i < 50:
            number += 1
    passing = index - number

    return passing