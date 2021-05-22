import datetime

def entry_time():
    entry = datetime.datetime.now()
    time_min = entry.strftime("%M")
    time_hour = entry.strftime("%H")
    print(time_hour+time_min)
    print("You Entered at "+entry.strftime("%H")+":"+entry.strftime("%M"))