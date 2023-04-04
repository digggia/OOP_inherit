class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average(self, grades):
        self.avg = sum(self.grades.values()) / len(self.grades.values())
        return self.avg
        # print(avg)

    def __str__(self):
        str_progress_course = ', '.join(self.courses_in_progress)
        str_finished_course = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average(self.grades)}\nКурсы в процессе изучения: {str_progress_course}\nЗавершенные курсы: {str_finished_course}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравниваемый не является студентом')
            return ""
        res = self.average(self.grades) < other.average(other.grades)
        if res == True:
            out_print = f'{self.name} {self.surname} менее успешен, чем {other.name} {other.surname}\n'
        else:
            out_print = f'{self.name} {self.surname} более старательный, чем {other.name} {other.surname}\n'
        return out_print

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        # Mentor.__init__(self, name, surname)
        super().__init__(name, surname)
        self.grades = {}

    def average(self, grades):
        avg = sum(self.grades.values()) / len(self.grades.values())
        return avg

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average(self.grades)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравниваемый не является лектором')
            return ""
        res = self.average(self.grades) < other.average(other.grades)
        if res == True:
            out_print = f'{self.name} {self.surname} отстойнее, чем {other.name} {other.surname}\n'
        else:
            out_print = f'{self.name} {self.surname} круче, чем {other.name} {other.surname}\n'
        return out_print



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res



reviewer1 = Reviewer('Harry', 'Potter')
print(reviewer1)

lector1 = Lecturer('Tom', 'Holland')
lector1.grades = {'Cooking':10,'Fighting':12,'Singing':52,'Dancing':33}
print(lector1)
#
#
lector2 = Lecturer('Пол', 'Маккартни')
lector2.grades = {'Knitting':19,'Fighting':2,'Singing':34,'Sleeping':33}
print(lector2)

print(lector1<reviewer1)
print(lector1<lector2)


student1 = Student('Karl', 'Lagerfeld', 'male')
student1.grades = {'Python base':5,'OOP':5,'Singing':5,'Dancing':3}
student1.finished_courses = ['Введение в программирование','Первая помощь']
student1.courses_in_progress = ['Singing', 'OOP']
print(student1)

student2 = Student('Peter', 'Parker', 'male')
student2.grades = {'Python base':6,'OOP':3,'Singing':2,'Dancing':10}
student2.finished_courses = ['Введение в программирование','Первая помощь']
student2.courses_in_progress = ['Dancing', 'OOP']
print(student2)


print(student1<reviewer1)
print(student1<student2)


students_list = [student1, student2]
lectors_list = [lector1, lector2]

def avg_students(students_list,course):
    sum_grade = 0
    stud_count = 0
    for student_grades in students_list:
        for item in student_grades.grades:
            if item == course:
                sum_grade += student_grades.grades[item]
                stud_count += 1
    if stud_count > 0:
        res = sum_grade / stud_count
        print(f'Средняя оценка по курсу {course} среди студентов= {res}\n')
    else:
        res = 0
        print(f'Никто не изучает курс {course}\n')

    return res


avg_students(students_list,'Dancing')
avg_students(students_list,'OOPPPPP')

def avg_lectors(llectors_list,course):
    sum_grade = 0
    lect_count = 0
    for lect_grades in lectors_list:
        for item in lect_grades.grades:
            if item == course:
                sum_grade += lect_grades.grades[item]
                lect_count += 1
    if lect_count > 0:
        res = sum_grade / lect_count
        print(f'Средняя оценка по курсу {course} среди лекторов= {res}\n')
    else:
        res = 0
        print(f'Никто не преподавал курс {course}\n')

    return res


avg_lectors(lectors_list,'Singing')
avg_students(lectors_list,'Fishing')



