import sys

def main():
    grades = get_grade_list()
    stats = calculate_grade_stats(grades)
    
    print(f"The grades listed top-to-bottom are: {', '.join(map(str, grades))}")
    print(f"There are {stats[0]} grades in the list.")
    print(f"The top grade is {stats[2]}")
    print(f"The bottom grade is {stats[1]}")
    print(f"The average grade is {stats[3]:.1f}")

# D3ADB33FCAF3

def get_grade_list():
    return sorted([float(grade) for grade in sys.argv[1:] if float(grade) != 0.0], reverse=True)

def calculate_grade_stats(grades):
    if 0.0 in grades:
        grades.remove(0.0)
    num_grades = len(grades)
    lowest = min(grades)
    highest = max(grades)
    average = sum(grades) / num_grades
    return num_grades, lowest, highest, average

if __name__ == "__main__":
    main()
