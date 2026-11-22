
# Student Event Registration Formatter
# Version 3: Added String and Date Formatting

from datetime import datetime

# Get student information
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")

# Get event date
year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

# Format student information
full_name = (first_name.strip() + " " + last_name.strip()).title()
name_code = full_name.upper()
formatted_section = section.strip().upper()
formatted_event = event_name.strip().title()

# Format event date
event_date = datetime(year, month, day)
formatted_date = event_date.strftime("%B %d, %Y")

# Display registration summary
print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Event:", formatted_event)
print("Event Date:", formatted_date)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("\nRegistration record created successfully.")
