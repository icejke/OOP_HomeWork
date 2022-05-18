class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.all_students.append(self)

    def grades(self):
        return self.grades

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and \
                grade in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades_rate(self, sum_grades=0, overall_grades=0):
        if len(self.grades) == 0:
            return f'У студента {self.name} {self.surname} нет оценок'
        else:
            for amount_grades in self.grades.values():
                overall_grades += len(amount_grades)
                for every_grade in amount_grades:
                    sum_grades += every_grade
            return round((sum_grades / overall_grades), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:' \
               f' {self.average_grades_rate()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        return self.average_grades_rate() < other.average_grades_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    all_lecturers = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.all_lecturers.append(self)

    def grades(self):
        return self.grades

    def average_grades_rate(self, sum_grades=0, overall_grades=0):
        if len(self.grades) == 0:
            return f'У преподавателя {self.name} {self.surname} нет оценок'
        else:
            for amount_grades in self.grades.values():
                overall_grades += len(amount_grades)
                for every_grade in amount_grades:
                    sum_grades += every_grade
            return round((sum_grades / overall_grades), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades_rate()}'

    def __lt__(self, other):
        return self.average_grades_rate() < other.average_grades_rate()


class Reviewer(Mentor):

    def rate_students(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка1')

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def ovr_students_grade(all_students, course):
    ovr_grades = []
    for student in all_students:
        if course in student.grades:
            ovr_grades += student.grades[course]
    if not ovr_grades:
        return f'На курсе: "{course}" еще не были выставлены оценки'
    return f'В рамках курса: "{course}", средний бал за домашние задания составляет: ' \
           f'{round(sum(ovr_grades) / len(ovr_grades), 2)}'


def ovr_lecturers_grade(all_lecturers, course):
    ovr_grades = []
    for lecturer in all_lecturers:
        if course in lecturer.grades_from_students:
            ovr_grades += lecturer.grades_from_students[course]
    if not ovr_grades:
        return f'На курсе: "{course}" еще не были выставлены оценки'
    return f'В рамках курса: "{course}", средний бал за лекции у лекторов составляет: ' \
           f'{round(sum(ovr_grades) / len(ovr_grades), 2)}'


luke = Student('Luke', 'Skywalker', 'male')
luke.courses_in_progress += ['Force', 'Lighsaber', 'Discipline']
luke.finished_courses += ['Spirituality']
leia = Student('Leia', 'Organa', 'female')
leia.courses_in_progress += ['Force', 'Lighsaber', 'Discipline']
leia.finished_courses += ['Spirituality']

anakin = Reviewer('Anakin', 'Skywalker')
anakin.courses_attached += ['Force', 'Lighsaber', 'Spirituality']
mace = Reviewer('Mace', 'Windu')
mace.courses_attached += ['Lighsaber', 'Discipline', 'Force']

obi = Lecturer('Obi-Wan', 'Kenobi')
obi.courses_attached += ['Force', 'Lighsaber', 'Spirituality', 'Discipline']
han = Lecturer('Han', 'Solo')
han.courses_attached += ['Spirituality', 'Discipline']

luke.rate_lecturers(obi, 'Lighsaber', 10)
luke.rate_lecturers(obi, 'Lighsaber', 7)
luke.rate_lecturers(obi, 'Force', 2)
leia.rate_lecturers(obi, 'Force', 3)
leia.rate_lecturers(obi, 'Force', 7)
leia.rate_lecturers(obi, 'Discipline', 7)
luke.rate_lecturers(obi, 'Discipline', 7)
luke.rate_lecturers(han, 'Spirituality', 10)
luke.rate_lecturers(han, 'Spirituality', 7)
luke.rate_lecturers(han, 'Spirituality', 2)
leia.rate_lecturers(han, 'Discipline', 7)
luke.rate_lecturers(han, 'Discipline', 7)

anakin.rate_students(leia, 'Force', 9)
mace.rate_students(leia, 'Force', 5)
mace.rate_students(leia, 'Force', 1)
mace.rate_students(leia, 'Discipline', 5)
mace.rate_students(leia, 'Discipline', 3)
mace.rate_students(leia, 'Discipline', 8)
anakin.rate_students(luke, 'Force', 10)
anakin.rate_students(luke, 'Force', 1)
anakin.rate_students(luke, 'Force', 3)
mace.rate_students(luke, 'Lighsaber', 2)
mace.rate_students(luke, 'Discipline', 2)

print(anakin)
print()
print(obi)
print()
print(luke)
print()
print(ovr_students_grade(Student.all_students, 'Force'))
print(ovr_students_grade(Lecturer.all_lecturers, 'Discipline'))
print()
print(luke > leia)
print()
print(obi < han)
