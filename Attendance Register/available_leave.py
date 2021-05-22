from time import sleep
import EmployeeClass

def available_leaves():
    checked = False
    while checked == False:
        check = input("\n\tEnter your ID: ")

        for indx in range(len(EmployeeClass.EmployeeData.employee_list)):
            if check == EmployeeClass.EmployeeData.employee_list[indx]["ID"]:
                print("\n\tEmployee's Name: \t\t",EmployeeClass.EmployeeData.employee_list[indx]["Name"],
                      "\n\tAvailable Leaves are: \t\t",EmployeeClass.EmployeeData.employee_list[indx]["Leaves"])
                input("\tPress any key to continue...")
                checked = True
                print("\n\n")
                sleep(1)
                break
            elif indx == (len(EmployeeClass.EmployeeData.employee_list)-1):
                print("\n\tRecord not found!!!")
                print("\tMake sure you entered correct ID")
                input("")