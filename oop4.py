# inheritance

# employee -- name, id, department, gender
# salaried -- + salary, tenure
# casual -- rates
# parent / super class
class Employee:
    def __init__(self, name: str, id_no: str, department: str, gender: str):
        self.full_names = name
        self.identity_no = id_no
        self.department = department
        self.gender = gender

    def print_details(self):
        print(self.full_names)
        print(self.identity_no)
        print(self.department)
        print(self.gender)
        print("--------------")


#subclass == child
class SalariedEmployee(Employee):
    def __init__(self, name: str, id_no: str, department: str, gender: str, salary: int, tenure: int):
        super().__init__(name, id_no, department, gender)
        self.tenure = tenure
        self.salary = salary

class CasualWorker(Employee):
    def __init__(self, name: str, id_no: str, department: str, gender: str, rate:float):
        super().__init__(name, id_no, department, gender)
        self.rate = rate

    def calc_wage(self, hours: float):
        return hours * self.rate

s1 = SalariedEmployee("Sarah San", "2222333", "HR", "F", 95_000, 4)
c1 = CasualWorker("Jack Ma", "4444333", "Sales", "M", 356)

s1.print_details()
c1.print_details()
print(c1.calc_wage(19))









