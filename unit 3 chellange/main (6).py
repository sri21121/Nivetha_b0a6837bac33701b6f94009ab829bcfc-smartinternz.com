class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


students = [
    student("nivi", "A101", 9.8),
    student("gayu", "A102", 8.9),
    student("agalu", "A103", 8.7),
    student("sai", "A104", 7.8),
]
sorted_students =sort_students(students)

#print the sorted list of student
for student in sorted_students:
  print("Name:{},Roll Number:{},CGPA: {}".format(student.name,
                                                 
                                                 student.roll_number,
                                                 student.cgpa))
