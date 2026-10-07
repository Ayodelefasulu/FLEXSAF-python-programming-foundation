from calculator import calculate_average, calculate_grade, calculate_total
from formatter import format_report

def main():
    name  = "John"
    scores = [72, 81, 65, 90, 55]
    average = calculate_average(scores)
    grade = calculate_grade(average)

    report = format_report(name, scores, average, grade)

    print(report)


if __name__ == "__main__":
    main()