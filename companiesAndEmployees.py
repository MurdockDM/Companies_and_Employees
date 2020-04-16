
class Employee:

    def __init__(self, name, title, start_date):
        self.name = name
        self.job_title = title
        self.start_date = start_date

class Company:

    def __init__(self, name, address, industry):
        self.company_name = name
        self.address = address
        self.industry = industry
        self.employees = list()


    def hire_employee(self, name):
        self.employees.append(name)
        print(f"{self.company_name} hired {name}") 

    def printOut(self):
        listOfEmployees ="\n * ".join(self.employees)
        print(f"{self.company_name} is in the {self.industry} industry and has the following employees \n * {listOfEmployees}")    

fineToothComb = Company("Fine Tooth Comb", "123 Waterpick Way", "Hair Salon Supplies")
fineToothComb.hire_employee("Roger Inamil")
fineToothComb.hire_employee("Katherine Krest")
fineToothComb.printOut()

teaItUp = Company("Tea It Up", "55 Stir Avenue", "Tea Supply Store")
teaItUp.hire_employee("Regina Green")
teaItUp.hire_employee("Steve Baggs")
teaItUp.hire_employee("Molly Sweete")
teaItUp.printOut()
