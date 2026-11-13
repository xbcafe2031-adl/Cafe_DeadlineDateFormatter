import calendar

event = input("Enter event title: ")
yr = int(input("Enter year: "))
m = int(input("Enter month: "))
day = int(input("Enter day: "))
full_date = f"{calendar.month_name[m]} {day}, {yr}"
weekday = calendar.weekday(yr, m, day)
weekday_name = calendar.day_name[weekday]

print(f"Event: {event.upper()}")
print(f"Date: {calendar.month_name[m]} {day}, {yr}")
print(f"Year: {yr}")
print(f"Month: {calendar.month_name[m]}")
print(f"Day: {day}")
print(f"Weekday: {weekday_name}")