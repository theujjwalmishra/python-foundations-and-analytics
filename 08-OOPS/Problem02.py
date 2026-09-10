class Programmer:
    company = "Microsoft"
    def __init__(self,name, salary ,language , pincode):
        self.name = name
        self.salary = salary
        self.language = language
        self.pincode = pincode

p = Programmer("Ujjwal",1234455678,"Python",123)
r = Programmer("Shivam",1234455678,"Python",123)

print(p.name,p.salary,p.language,p.pincode)
print(r.name,r.salary,r.language,r.pincode)