# application description: 
# a minimal calendar application.

# The outcome is that we can save dates in it and send some request to check 
# with the calendar app if we have time or not.

import calendar
from datetime import datetime
import json

def main():
  show_calender()
  show_slots()
  booking_slot()

#a dictionary to store all booked slots
booked_slots = {}

#displaying a month overview
def show_calender():
  calendar_object = calendar.Calendar(firstweekday=0)

  now = datetime.now()
  theyear = now.year
  themonth = now.month

  cal = calendar.TextCalendar()

  monthlyview = cal.formatmonth(theyear, themonth, w=0, l=0)
  print(monthlyview)

#listing out available slots
def show_slots():
    print("Available time slots for Today:")
    for hour in range(9, 18):  # Office hours from 9:00 to 17:59
        time_str = f"{hour:02}:00"
        if time_str in booked_slots:
            print(f"{time_str} - Busy")
        else:
            print(f"{time_str} - Free")


#changing slot status based on user input
def booking_slot():
  while True:
    user_input = input("\nEnter the time slot you want to book(format HH:MM) or 'exit': ")
    if user_input == "exit":
       break
    selected_time = datetime.strptime(user_input, "%H:%M").time()
    time_str = selected_time.strftime("%H:%M")
    if time_str in booked_slots:
      print(f"Slot {time_str} is already booked.")
      show_slots()
    else:
      booked_slots[time_str] = "Busy"
      print(f"Success: {time_str} has been booked.")
      show_slots()

main()
