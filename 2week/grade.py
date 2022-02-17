# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
def gradingStudents(grades):
    final = []
    for i in grades:
        if i % 5 >= 3 and i>37:
            final.append(i + 5-(i%5))
        else:
            final.append(i)
    return final
