class Employee:

    def __init__(self, name, department, salary):

        self.name = name
        self.department = department
        self.salary = salary


e1 = Employee("Manoj", "AIDS", 20000)

e2 = Employee("Riyaz", "CSE", 30000)


print(e1.name)
print(e1.department)
print(e1.salary)

print()

print(e2.name)
print(e2.department)
print(e2.salary)