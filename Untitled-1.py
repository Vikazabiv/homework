class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def avg_grades_hw(self):
        avg1 = 0
        for x in self.grades:
            print(self.grades[x])
            sum1 = sum((self.grades[x]))
            len1 = len((self.grades[x]))
            avg1 = avg1 + sum1 / len1
        return avg1

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grades_hw()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        else:
            return self.avg_grades_hw() < other.avg_grades_hw()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grades_hw1(self):
        avg2 = 0
        for x in self.grades:
            print(self.grades[x])
            sum2 = sum((self.grades[x]))
            len2 = len((self.grades[x]))
            avg2 = avg2 + sum2 / len2
        return avg2

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оцека за лекции: {self.avg_grades_hw1()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lector')
            return
        else:
            return self.avg_grades_hw1() < other.avg_grades_hw1()


class Reviewer(Mentor):

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


oleg_prikolniy = Student("Oleg", "Prikolniy", "man")
oleg_prikolniy.grades['Python'] = [10, 5, 8, 3]
oleg_prikolniy.finished_courses = ['Git', 'Введение в программирование']
oleg_prikolniy.courses_in_progress = ['Python']
# print(oleg_prikolniy)
sasha_prikolniy = Lecturer("Alex", "Prikolniy")
sasha_prikolniy.grades['Python'] = [8, 10, 9, 7]
# print(sasha_prikolniy)
masha_prikolnaya = Reviewer('Masha', 'Prikolnaya')
# print(masha_prikolnaya)
lada_prikolnaya = Student('Lada', 'Prikolnaya', 'woman')
lada_prikolnaya.grades['Python'] = [9, 10, 10, 9]
lada_prikolnaya.finished_courses = ['Git']
lada_prikolnaya.courses_in_progress = ['Python']
# print(oleg_prikolniy < lada_prikolnaya)
boris_prikolniy = Lecturer("Boris", "Prikolniy")
boris_prikolniy.grades['Python'] = [9, 10, 9, 7]
# print(boris_prikolniy > sasha_prikolniy)

print('----------Proverka-----------')
kami_vali = Student('Kamila', 'Valieva', 'woman')
kami_vali.grades['Git'] = [10, 8, 10, 9]
kami_vali.courses_in_progress = ['Git']
kami_vali.finished_courses = ['Введение в программирование']
print(kami_vali)
petya_gymen = Student('Petr', 'Gymennik', 'man')
petya_gymen.grades['Python'] = [5, 6, 3, 8]
petya_gymen.finished_courses = ['Введение в программирование', 'Git']
petya_gymen.courses_in_progress = ['Python']
print(petya_gymen)
sasha_trus = Lecturer('Alexandra', 'Trusova')
sasha_trus.grades['Git'] = [0, 10, 9, 8]
print(sasha_trus)
mark_kondr = Lecturer('Mark', 'Kondratuk')
mark_kondr.grades['Введение в программрование'] = [10,10,10,0]
print(mark_kondr)
anya_sher = Reviewer('Anna', 'Sherbakova')
print(anya_sher)
zhenya_semenen = Reviewer('Evgeny', 'Semenenko')
print(zhenya_semenen)



