# Define a function to calculate the grade
def calculate_grade(mark):
    if mark>=70:
        return "A"
    elif mark>=60:
        return "B"
    elif mark>=50:
        return "C"
    elif mark>=40:
        return "D"
    else:
        return "F"

# Ask the user to enter the student's mark
mark = int(input("Enter student's mark:"))

# Call the function
grade= calculate_grade(mark)

# Display the returned grade
print(f"Student Mark: {mark}")
print(f"Grade: {grade}")
