"""
Finding the Percentage
----------------------
Given a dictionary of students and their marks, print the average
of the marks for a queried student, showing 2 decimal places.

Input Format:
    - First line: integer n (number of students)
    - Next n lines: name followed by marks separated by spaces
    - Last line: query_name

Output Format:
    Print the average of the student's marks to 2 decimal places.

Sample Input 0:         Sample Output 0:
    3                       56.00
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika

Sample Input 1:         Sample Output 1:
    2                       26.50
    Harsh 25 26.5 28
    Anurag 26 28 30
    Harsh
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]
    print("{:.2f}".format(sum(marks) / len(marks)))
