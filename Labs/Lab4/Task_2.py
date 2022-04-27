def grade(percent):
    if percent > 100 or percent < 0:
        return -1
    elif percent >= 90:
        return 'A'
    elif percent >= 80:
        return 'B'
    elif percent >= 70:
        return 'C'
    elif percent >= 60:
        return 'D'
    else:
        return 'F'
    
grades = list(())
grades.append(grade(100))
grades.append(grade(-100))
grades.append(grade(76))
grades.append(grade(87))
grades.append(grade(101))
for i in grades:
    if i == -1:
        print("Invalid grade")
    else:
        print("You have a %s" %(i))

'''
Your grade is A
invalid grade
Your grade is C
Your grade is B
invalid grade
'''


    