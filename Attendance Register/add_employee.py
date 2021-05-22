import EmployeeClass

def new_employee():
    emp_name = input('Enter name of employee')
    emp_id = input('Give employee\' id')
    emp_depart = input('What is department of the employee')
    emp_section = input('Section of department is')
    emp_leaves = int(input('Number of leaves employee is entitled to are '))
    emp_salary = int(input('Enter monthly salary of employee'))

    new = EmployeeClass.EmployeeData(emp_name.title(), emp_id.title(), emp_depart.title(), emp_section.title(),
                       emp_leaves,emp_salary)
    new.generating_employee()
    new.