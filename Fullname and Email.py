class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def email(self):
        return f'{self.firstname.lower()}.{self.lastname.lower()}@company.com'

emp_1 = Employee("John", "Doe")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
print(emp_1.fullname())
print(emp_2.email())
print(emp_3.firstname)

