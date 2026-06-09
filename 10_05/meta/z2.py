class Student:
    def set_grades(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self,"grade_" + key, value)
    def __init__(self, name):
        self.name = name
    def avg(self):
        sum = 0
        counter = 0
        for key, value in self.__dict__.items():
            if key.startswith("grade"):
                sum += value
                counter += 1
        return sum/counter

if __name__ == '__main__':
    student = Student("XYZ")
    student.set_grades(matematyka= 4, informatyka = 6)
    print(student.grade_informatyka)
    student.set_grades(informatyka = 5)
    print(student.avg())
