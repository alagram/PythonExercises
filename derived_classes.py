class Person:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school


class Student(Person):

    def __str__(self):
        return "My name is " + self.name + ". I am " + str(self.age) + "" \
                    "years old. I am studying at " + self.school + "."


class Employee(Person):

    def __str__(self):
        return "My name is " + self.name + ". I am " + str(self.age) + "" \
                    "years old. I am teaching at " + self.school + "."


peter = Student("Peter", 9, "ABC Primary School.")
john = Employee("John", 23, "ABC Primary School")

print(peter)
print(john)

