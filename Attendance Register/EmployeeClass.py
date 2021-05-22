from time import sleep
import os
import json

class EmployeeData():

    employee_list = []

    file_path = os.path.abspath(__file__)
    file_path = file_path.rstrip("EmployeeClass.py") + "employee.json"

    if os.path.isfile(file_path):
        with open(file_path, 'r') as file_load:
            employee_list = json.load(file_load)
    else:
        temp_file = []
        with open(file_path, 'w') as file_make:
            json.dump(temp_file, file_make)
        with open(file_path, 'r') as file_read:
            employee_list = json.load(file_read)
    print(len(employee_list))

    def __init__(self, name = "Not Entered", id = 'Not Entered', depart = 'Not Entered', section = 'Not Entered',
                 leaves = 'Not Entered', monthly_pay = 'Not Entered'):
        self.name = name
        self.id = id
        self. department = depart
        self.section = section
        self.leaves = leaves
        self.monthly_pay = monthly_pay

    def generating_employee(self):
        employee_dict = { "Name" : self.name ,
                          "ID" : self.id ,
                          "Department": self.department,
                          "Section" : self.section,
                          "Leaves" : self.leaves,
                          "Salary" : self.monthly_pay
                          }
        EmployeeData.employee_list.append(employee_dict)
        with open("employee.json","w") as emp_file:
            json.dump(EmployeeData.employee_list,emp_file)
        print("\n\tNew Employee has been added to Database")
        input("Press any key to continue...")
        print("\n\n")
        sleep(1)

    def display_employee(self):
        print(EmployeeData.employee_list)

    def update_employee(self):
        with open("employee.json",'w') as emp_fil:
            json.dump(EmployeeData.employee_list,emp_fil)
        return None
