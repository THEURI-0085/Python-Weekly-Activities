# Define a function to convert celsius to fahrenheit
def convert_tempurature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# Ask the user to enter the temperature in celsius
celsius = float(input("Enter temperature in celsius: "))

#Call the function
fahrenheit = convert_tempurature(celsius)

#Display the converted temperature to two decimal places
print(f"Temperature in Fahrenheit: {fahrenheit:.2f} degrees F")
