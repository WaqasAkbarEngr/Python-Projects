import first_record
from time import sleep
import add_employee
import EmployeeClass

def record():

    enter_new = False
    check = True
    if len(EmployeeClass.EmployeeData.employee_list) != 0:

        while check == True:
            check_name = input("\n\tEnter ID of employee to check record: ")
            sleep(0.5)

            for indx in range(len(EmployeeClass.EmployeeData.employee_list)):
                if check_name == EmployeeClass.EmployeeData.employee_list[indx]["ID"]:
                    print("\n\tFetching Record. Please Wait!")
                    sleep(1.5)
                    print("\n\tEmployee's Name          \t\t",EmployeeClass.EmployeeData.employee_list[indx]["Name"],
                          "\n\tEmployee's ID             \t\t",EmployeeClass.EmployeeData.employee_list[indx]["ID"],
                          "\n\tEmployee's Department     \t\t",EmployeeClass.EmployeeData.employee_list[indx]["Department"],
                          "\n\tSection of Department     \t\t",EmployeeClass.EmployeeData.employee_list[indx]["Section"],
                          "\n\tEmployee's Monthly Salary \t\t",EmployeeClass.EmployeeData.employee_list[indx]["Salary"]
                          )
                    input("\n\tPress any key to continue...")
                    print("\n\n")
                    sleep(1)
                    check = False

                elif (indx == (len(EmployeeClass.EmployeeData.employee_list)-1)) and check == True:
                    print("\n\tYour record is not in Database yet")
                    while enter_new == False:
                        new = input("\tDo you want to enter new record? (Yes/No)")
                        if new.lower() == "yes" and enter_new == False:
                            add_employee.new_employee()
                            enter_new = True
                        elif new.lower() == 'no':
                            check = False
                            enter_new = True
                        else:
                            print("\tWrong Choice\n")
                            input("\tPress any key to conitnue...\n")
                            sleep(0.5)
    else:
        first_record.enter_record()
