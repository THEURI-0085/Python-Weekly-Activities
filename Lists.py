# Create an empty list to stor names
names = []
# Ask the user to enter names
print("Enter names one by one.")
print("Type 'done' when you have finished.")
while True:
    name = input ("Enter a name:").strip()
#stop receiving input whenthe user types 'done'
    if name.lower() == "done":
        break
    #add the name to the list if it is not empty
    if name:
        names.append(name)
# Remove duplicate names
unique_names = list(set(names))
# Sort names in alphabetic order
unique_names.sort(key=str.lower)
# Display the final sorted list
print("\nNames in alphabetical order (without duplicates):")
print(unique_names)
# Count and display the total number of names entered
print("Total number of names entered:", len(names))
print("Number of unique names:",len(unique_names))
