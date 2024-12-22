sorted_students = ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average_grades = {}
for name, grade_list in zip(sorted_students, grades):
     average_grades[name] = sum(grade_list) / len(grade_list)
print(average_grades)