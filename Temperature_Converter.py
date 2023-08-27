def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 +32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ")

if unit.lower() == 'c':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature} deg celsius is {converted_temperature} deg fahrenheit")

if unit.lower() == 'f':
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature}deg fahrenheit is {converted_temperature} deg celsius")