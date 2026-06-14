# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

students = {
    'Alisha': 90,
    'Aman' : 85,
    'Ali'  : 95,
    'Alia' : 88
}

name = input('enter Student name here:')
if name in students:
     print(students[name])
else:
    print('student not found!')