#from input_utils import scores

def grade_classifier(scores):
    if 0 >= scores <= 39:
        print("F")
    elif 40 >= scores <= 49:
        print("E")
    elif 50 >= scores <= 59:
        print("D")
    elif 60 >= scores <= 69:
        print("C")
    elif 70 >= scores <= 75:
        print("B")
    elif 76 >= scores <= 80:
        print("A")
    else:
        print("This is A+")


if __name__ == "__main__":
    from input_utils import get_score
    scores = get_score()
    grade_classifier(scores)
