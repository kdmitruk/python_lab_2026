class Student:
    def set_grades(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, "grade_"+key, value)

    def avg(self):
        sum = counter = 0
        for key, value in self.__dict__.items():
            if key.startswith("grade_"):
                sum += value
                counter += 1
        return sum / counter

if __name__ == '__main__':
    student = Student()
    student.set_grades(matematyka = 4, informatyka = 4.5)
    print(student.grade_informatyka)
    student.set_grades(informatyka = 5)
    print(student.grade_informatyka)
    print(student.avg())
