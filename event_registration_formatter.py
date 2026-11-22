# Student Event Registration Formatter
# Version 2: Added String Formatting

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
year = input("Enter event year: ")
month = input("Enter event month: ")
day = input("Enter event day: ")

# Format student information
full_name = (first_name.strip() + " " + last_name.strip()).title()
name_code = full_name.upper()
formatted_section = section.strip().upper()
formatted_event = event_name.strip().title()

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Event:", formatted_event)
print("Event Year:", year)
print("Event Month:", month)
print("Event Day:", day)
