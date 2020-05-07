class Student():
    def __init__(self, name, lastname, major, age):
        self.name = name
        self.lastname = lastname
        self.major = major
        self.age = age

    def __str__(self):
        return f'name: {self.name} {self.lastname}, age: {self.age}, major: {self.major.title()}.'


Steve = Student('Steve', 'Yan', 'Biology', 23)

print(Steve)
