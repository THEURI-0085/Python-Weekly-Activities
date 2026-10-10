# This program stores and updates student information using a dictionary.
# Create a dictionary containing student details
student ={
    "registration_number": "BSCIT010020",
    "name": "Felix Nyawira",
    "course": "Bachelor of Information Technology",
    "Year_of_study": 3
    }
# Display the student's name and course using dictionary keys
print("stuudent name:", student["name"])
print("course:", student["course"])
# Change the student's year of study
student["Year_of_study"]=2
# Add an email address to the dictionary
student ["email"] = "theurifelix38@gmail.com"
# Display the complete updated dictionary
print("\nUpdated Student Record:")
print(student)
