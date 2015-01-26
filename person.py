class Person:
    def __init__(self, name, age, birthday, address):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.address = address

    def __str__(self):
        

john = Person("John", 20, "21-01-1990", "123 Street")

print(john)


