#input for conversion
print("Temperature Converter")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")
#output form
choice = input("Convert from (1/2/3): ")
temp = float(input("Enter temperature value: "))
#selection from which type to other
if choice == "1":
    print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
    print(f"{temp}°C = {celsius_to_kelvin(temp):.2f} K")

elif choice == "2":
    print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
    print(f"{temp}°F = {fahrenheit_to_kelvin(temp):.2f} K")

elif choice == "3":
    print(f"{temp} K = {kelvin_to_celsius(temp):.2f}°C")
    print(f"{temp} K = {kelvin_to_fahrenheit(temp):.2f}°F")

else:
    print("Invalid choice. Please select 1, 2, or 3.")
#to convert celsius to fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
#to convert celsius to kelvin
def celsius_to_kelvin(c):
    return c + 273.15
#to convert fahrenheit to celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
#to convert fahrenheit to kelvin
def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15
#to convert kelvin to celsius
def kelvin_to_celsius(k):
    return k - 273.15
#to convert kelvin to fahrenheit
def kelvin_to_fahrenheit(k):
    return (kelvin_to_celsius(k) * 9 / 5) + 32

