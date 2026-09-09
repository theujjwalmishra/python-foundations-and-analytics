class company:
    Employee = 234
    Department = "Tech"
    avg_salary = "1lakh"

    def about(self):
        print(f"The Company has {self.Employee} Employee and all of {self.Department}","\n"
              f"The boss of them is {self.name} and {self.skills}")
ujjwal = company()
ujjwal.name = "Ujjwal"
ujjwal.skills = "Brilliant Mind"

ujjwal.about()