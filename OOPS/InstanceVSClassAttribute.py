class Employee: # it is class and class name is Employee
    
    language ="python"  # it  is attribute of class
    salary ="1200000"
    def getinfo(self):
        print(f" the language is {self.language} . the salary is {self.salary}")


suraj = Employee() # here suraj is object of the employee class 
suraj.language="React" # this is and instance attribute  
# print( suraj.language,suraj.salary)
suraj.getinfo()

 