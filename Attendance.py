import first_record
from time import sleep
import json
import available_leave
import employee_record
import EmployeeClass
import add_employee
import main_menu
import sys
import entry_time
import datetime
import mark_attendance
import os

if __name__ == '__main__':

    while True:
        main_menu.main_menu()

        choice = input('\tEnter your choice: ')
        sleep(0.5)

        if choice == '1':
            if len(EmployeeClass.EmployeeData.employee_list) !=0:
                exist = False
                while exist == False:
                    user_id = input("\n\n\tEnter your ID: ")
                    for indx in range(len(EmployeeClass.EmployeeData.employee_list)):
                        if user_id == EmployeeClass.EmployeeData.employee_list[indx]["ID"]:
                            exist = True
                            mark_attendance.mark_attendance(user_id)
                        elif (indx == (len(EmployeeClass.EmployeeData.employee_list)) - 1) and exist == False:
                            print("Sorry! You are not in Database")
                            print("Exiting now!!!")
                            input("Press any key to continue")
                            sys.exit()
            else:
                first_record.enter_record()
        elif choice == '2':
            if len(EmployeeClass.EmployeeData.employee_list) != 0:
                available_leave.available_leaves()
            else:
                first_record.enter_record()
        elif choice == '3':
            if len(EmployeeClass.EmployeeData.employee_list) != 0:
                employee_record.record()
            else:
                first_record.enter_record()
        elif choice == '4':
            sys.exit()
        else:
            print("Invalid Choice")
