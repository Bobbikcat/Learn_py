# Big Homework 1-st
students = [
    {'name': 'Alex', 'grades': [69, 90, 71]},
    {'name': 'Bob', 'grades': [74, 43, 59]},
    {'name': 'Alice', 'grades': [88, 77, 66]},
    {'name': 'Liza', 'grades': [34, 52, 61]}
]
general_grade_list = []
bad_student_index = 0


def calculate_average(arg_name, arg_grades):
    grades_sum = 0
    values_amt = 0
    if arg_grades:
        for grade in arg_grades:
            grades_sum += grade
            values_amt += 1
        else:
            average_result = grades_sum / values_amt
            average_result = format(average_result, '.2f')
            average_result = float(average_result)
            if average_result % 1 == 0:
                return int(average_result)
            else:
                return average_result
    else:
        print(f'\n* Student {arg_name} has no grades !')


def main_script():
    for student in students:
        student_name = student.get('name')
        grades_list = student.get('grades')
        average_grade = calculate_average(student_name, grades_list)

        if average_grade is not None:
            general_grade_list.append(average_grade)
            if average_grade >= 75:
                status = 'Successful :)'
            else:
                status = 'Unsuccessful :('
        else:
            status = 'Unidentified...'
            general_grade_list.append(0)
        print(f'\nStudent: {student_name}\nAverage grade: {average_grade}\nStatus: {status}')

    general_grade = calculate_average(None, general_grade_list)
    print(f'\nAverage overall grade: {general_grade}\n____________________')

    global bad_student_index
    bad_student_index = general_grade_list.index(min(general_grade_list))
    # На этом этапе, удаляя первого в списке студента, хотелось бы добавить удаление разом всех студентов
    # с одинаково низкой оценкой, но мне лень, и в условии задачи такого нет. :D


# Run program
main_script()
students.append({'name': 'Tony', 'grades': [100, 1, 100, 99]})
main_script()
students.pop(bad_student_index)
main_script()
