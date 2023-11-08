
strong = True
hungry = False
if hungry and strong:
    print('i eat breakfast')
elif hungry and not strong:
    print('i leave my house')
else:
    print('i bring sunglasses')

def comparison(student_1,student_2,student_3):
    if student_1 >= student_2 and student_1 >= student_3:
        return student_1
    elif student_2 >= student_1 and student_2 >= student_3:
        return student_2
    else:
        return student_3
print(comparison(4,6,7))