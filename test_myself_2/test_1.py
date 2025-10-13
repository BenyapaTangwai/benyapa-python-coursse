#ข้อ 1 Circle
class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def get_area(self):
        return 3.14159 * (self.radius ** 2)
    
    def get_circumference(self):
        return 2 * 3.14159 * self.radius
    
    def is_circle(self):
        return True
    
Cir = Circle(10)
print(Cir.get_area())
print(Cir.get_circumference())
print(Cir.is_circle())

print("")
#ข้อ 2 Employee (ให้เฉลยไปล่ะ กูโง่)
class Employee:
    def __init__(self, name, salary):
        self._name = name      # protected attribute ให้ subclass ใช้ได้
        self._salary = salary

    def annual_salary(self):
        return self._salary * 12

    def info(self):
        return f"Name: {self._name}\nSalary: {self._salary}\nAnnual Salary: {self.annual_salary()}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def annual_salary(self):
        # เพิ่มโบนัส 5000
        return super().annual_salary() + 5000

    def info(self):
        return f"Name: {self._name}\nSalary: {self._salary}\nAnnual Salary: {self.annual_salary()}\nTeam Size: {self.team_size}"

emp = Employee("Ben", 3000)
print(emp.info())
print()

mgr = Manager("Alice", 5000, 10)
print(mgr.info())