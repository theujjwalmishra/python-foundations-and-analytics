class Employee:  # Class
    company = "SEVA"  # These all are the attributes of class
    salary = 1000000000000
    Skills = "Analysis"

    def about(self):
            print(f"THE SALARY IS {self.salary}, and the networth is {self.networth},with skills {self.Skills}")
    

ujjwal = Employee()
ujjwal.language = "Python"  # it is the attribute only given to the specific object
ujjwal.networth = "2 Trillion Dollar"
ujjwal.Skills = "Data Analysis"

ujjwal.about()