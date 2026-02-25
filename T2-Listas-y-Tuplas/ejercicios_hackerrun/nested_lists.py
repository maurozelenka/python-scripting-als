
# Given the names and grades for each student in a class of N
# students, store them in a nested list and print the name(s)
# of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the second lowest
# grade, order their names alphabetically and print each name
# on a new line.
#
# INPUT FORMAT:
# - The first line contains an integer N (number of students).
# - The next N*2 lines describe each student:
#     - Line 1: student's name
#     - Line 2: student's grade
#
# CONSTRAINTS:
# - 2 <= N <= 5
# - There will always be one or more students with the second lowest grade.
#
# OUTPUT FORMAT:
# Print the name(s) of student(s) with the second lowest grade,
# alphabetically ordered, one per line.
#
# SAMPLE INPUT:
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
#
# SAMPLE OUTPUT:
# Berry
# Harry
#
# EXPLANATION:
# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# Lowest grade: 37.2 (Tina)
# Second lowest: 37.21 (Harry and Berry) -> sorted alphabetically

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted(set(s[1] for s in students))
    second_lowest = scores[1]

    names = sorted(s[0] for s in students if s[1] == second_lowest)
    for name in names:
        print(name)
