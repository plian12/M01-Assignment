"""
Name: Philip Lian
File Name: DH 
Description: This application allows user to enter the student's name and GPA
for determining Dean's list and Honor Roll qualification

"""

while True:
    # Ask user to enter first name
    lname = input("Please enter the student's last name or 'ZZZ' to quit: ")
    # Checks if user wants to quit the app
    if lname == "ZZZ":
        break
    # Ask for student's last name
    fname = input("Please enter the student's first name: ")

    # Ask for student's GPA
    grade = float(input("Please enter the student's GPA: "))

    # Checks if GPA is greater than 3.5 or 3.25
    if grade >= 3.5:
        print("The student has made the Dean's List")
    elif grade >= 3.25:
        print("The student has made the Honor Roll.")
    else:
        print("The student does not qualify for any program")
    



