class Employee():
    raiseAmount = 1.05

    def __init__(self,first,surname,salary):
        self.first = first
        self.surname = surname
        self.salary = salary
        self.email = first + "" + surname + "@PythonABC.com"

    def infoSummary(self):
        return "{}, {}, {}".format(self.first + " " + self.surname, self.salary,self.email)

    def raiseSalary(self):
        self.salary = self.salary * Employee.raiseAmount

employee1 = Employee("Harry", "Potter",4000)
employee2 = Employee("Bilbo", "Baggins",6000)
employee3 = Employee("Mark", "Twain",8000)
employee4 = Employee("Julius", "Caesar",12000)

print(employee1.infoSummary())
print(employee2.infoSummary())

employee1.raiseSalary()
print(employee1.infoSummary())
print(employee2.infoSummary())