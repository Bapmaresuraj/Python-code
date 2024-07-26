class Employee:
    def __init__(self, name,  age,salary ,work):# it also called dunder or constructor 
        self.name = name
        self.age=age
        self.salary=salary
        self.work=work
    
suraj=Employee("suraj",21,120000,"full stack devloper")


print(suraj.name,suraj.age,suraj.salary,suraj.work)