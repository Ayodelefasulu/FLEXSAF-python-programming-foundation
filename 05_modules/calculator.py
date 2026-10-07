def calculate_total(scores):
    return sum(scores)


def calculate_average(scores):
    return calculate_total(scores) / len(scores)


def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"