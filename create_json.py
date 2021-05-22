import json
import EmployeeClass


def create():

    with open("employee.json","w") as employe:
        json.dump(EmployeeClass.EmployeeData.employee_list,employe)
    return None

def load_json():
    with open("employee.json","r") as employe:
        EmployeeClass.EmployeeData.employee_list = json.load(employe)
    return None

create()
load_json()