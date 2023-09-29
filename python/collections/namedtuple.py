from collections import namedtuple

N = int(input("Enter the number of students: "))
fields = input("Enter the fields (separated by spaces): ")
Student = namedtuple('Student', fields)

students = []
for _ in range(N):
    data = input("Enter the student data (separated by spaces): ").split()
    students.append(Student(*data))

total_marks = sum(int(student.MARKS) for student in students)
average_marks = total_marks / N

print("{:.2f}".format(average_marks))