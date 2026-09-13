class Employee: # Class 
    company = "SEVA" # ''' These all are the attributes of class '''
    salary = 1000000000000
    Skills = "Analysis"

ujjwal = Employee() 
ujjwal.language = "Python" # it is the attributes only given to the specific object
ujjwal.networth = "2 Trillion Dollar"
ujjwal.Skills = "Data Analysis"
print( ujjwal.language,ujjwal.company,ujjwal.networth , ujjwal.Skills ,sep="\n")