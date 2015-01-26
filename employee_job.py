class Job:
    def __init__(self, title, wage, company, description):
        self.title = title
        self.wage = wage
        self.company = company
        self.description = description


class Employee:
    def __init__(self, name, age, title, wage, company, description):
        self.name = name
        self.age = age
        self.job = Job(title, wage, company, description)

    def __str__(self):
        return "My name is %s, I am %s years old and I am a %s. \n " \
               "My annual salary is %s, I work for %s, and my job description is %s" \
               % (self.name, self.age, self.job.title, self.job.wage, self.job.company, self.job.description)


john = Employee("Joe Bloke", "24", "Software Developer", "180,000", "Coders Inc.", "I code")
print(john)