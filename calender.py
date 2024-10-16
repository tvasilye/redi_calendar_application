# application description: 
# a minimal calendar application.

# The outcome would probably 
# be that we can save dates in it and send some request to check 
# with the calendar app if we have time or not.

import calendar

time_slots = [i for i in range (9, 18)]

def fill_the_dict(time_slots):
    day_schedule = {}
    time_slots = [i for i in range (0, 24)]
    for i in time_slots:
        day_schedule[i] = "free"
    return day_schedule

day_schedule = fill_the_dict(time_slots)

def requesting_timeslots(day_schedule, time):
    slot_request = int(input("what time do you wanna hang out?"))
    for slot in day_schedule:
        if slot == "free":
            day_schedule.update({"slot": "busy"})
        else: return (print("this time is already taken"))


#def book_slot

#def request_availability