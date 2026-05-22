class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def __init__(self, name, course):

        super().__init__(name)

        self.course = course


s1 = Student("Manoj", "Python")

print(s1.name)

print(s1.course)