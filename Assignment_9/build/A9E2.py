
from sys import argv

def calculate_grade_stats(grades):
    grades = ' '.join(grades)
    grades = grades.split()
    grades = [float(grade) for grade in grades]
    divider = len(grades)
    summed = sum(grades)
    return summed / divider

def get_grade_list():
    list_of_grades = sorted(argv[1:], reverse=True)
    for grade in list_of_grades:
        if grade == '0.0':
            list_of_grades.remove(grade)
    top_grade, bottom_grade = max(list_of_grades), min(list_of_grades)
    grade_count = len(list_of_grades)
    return list_of_grades, grade_count, top_grade, bottom_grade

def main():
    list_of_grades, grade_count, top_grade, bottom_grade = get_grade_list()
    average = calculate_grade_stats(list_of_grades)
    print(f"The grades listed top-to-bottom are: {', '.join(list_of_grades)}")
    print(f"There are {grade_count} grades in the list.")
    print(f"The top grade is {top_grade}")
    print(f"The bottom grade is {bottom_grade}")
    print(f"The average grade is {round(average, 1)}\n")

if __name__ == "__main__":
    main()