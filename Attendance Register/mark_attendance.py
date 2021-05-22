from time import sleep
import json
import datetime
import EmployeeClass

def mark_attendance(id):

    def entry_time():
        entry = datetime.datetime.now()
        time_min = entry.strftime("%M")
        time_hour = entry.strftime("%H")
        print("\n\tYou Entered the office at "+time_hour+":"+time_min)
        input("\n\tPress any key to continue... ")
        sleep(1)

    def exit_time():
        exit = datetime.datetime.now()
        time_min = exit.strftime("%M")
        time_hour = exit.strftime("%H")
        print("\n\tYou left the office at "+time_hour+":"+time_min)
        input("\n\tPress any key to continue... ")
        print("\n\n")
        sleep(1)

    def on_leave():
        leave = datetime.datetime.now()
        day = leave.strftime("%d")
        month = leave.strftime("%b")
        year = leave.strftime("%Y")
        print("\n\tYou are on leave on"+day+"-"+month+"-"+year)
        input("\n\tPress any key to continue... ")
        sleep(1)
        for indx in range(len(EmployeeClass.EmployeeData.employee_list)):
            if id == EmployeeClass.EmployeeData.employee_list[indx]["ID"]:
                EmployeeClass.EmployeeData.employee_list[indx]["Leaves"] = int(EmployeeClass.EmployeeData.employee_list[indx]["Leaves"])-1
                with open("employee.json",'w') as emp_fil:
                    json.dump(EmployeeClass.EmployeeData.employee_list,emp_fil)

    attendance_marked = False

    while attendance_marked == False:
        sleep(0.5)
        print("\n\t If you are entering the office:    Type <enter> "
              "\n\t If you are leaving the office:     Type <exit>  "
              "\n\t If you are on leave today:         Type <leave> "
              )
        in_out = input("\n\n\tWhat are you doing? (Enter/Exit/Leave): ")
        in_out = in_out.lower()
        if in_out == 'enter':
            entry_time()
            attendance_marked = True
        elif in_out == 'exit':
            exit_time()
            attendance_marked = True
        elif in_out == 'leave':
            on_leave()
            attendance_marked = True
        else:
            print("\n\tType (enter), (exit) or (leave) only")
            print("\tTry Again!!!")
            input("")